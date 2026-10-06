---
name: macos-app-wont-open
description: 诊断并修复 macOS 上「应用已安装但打不开」的问题（Gatekeeper 拦截、隔离属性异常、签名/架构不兼容、启动即退出）。当用户说「App 打不开」「提示无法打开」「已损坏，无法打开，应该将它移到废纸篓」「无法验证开发者」「Apple 无法检查是否包含恶意软件」「双击没反应」「图标跳一下就没了」「装好了但启动不了」时使用。核心是分层定位：完整性 → 架构 → 签名 → Gatekeeper 评估 → 隔离属性 → 实际启动，逐层排除，不靠猜。
agent_created: true
---

# macOS 应用「打不开」分层诊断

## 核心原则

1. **先分层取证，再下结论**。同一个「打不开」可能是 5 种完全不同的原因，处理方式互不通用。
2. **签名有效 ≠ 能启动**。Gatekeeper 的隔离属性（quarantine）可以在签名完全正常的情况下拒绝执行。
3. **沙盒外复跑一次**。工具自带沙盒会污染诊断结果，关键结论必须在沙盒外（`dangerouslyDisableSandbox`）复核。
4. **先只读诊断，改文件前把结论说清楚**。

## 五层诊断法

按顺序排查，任一层失败即锁定根因，不必往下走。

### 第 0 层：定位目标

```bash
ls -d /Applications/*[Xx]xx* 2>/dev/null
mdfind -name "<关键词>" | head -30
mdfind "kMDItemKind == Application" | grep -i <关键词>
```

注意区分：**`.dmg.download` 是 Safari 未完成的下载临时目录**（内含 `Info.plist` + 部分文件），不是可用安装包。看到它就说明下载还没结束。

### 第 1 层：完整性

```bash
APP="/Applications/Foo.app"
du -sh "$APP"
ls -la "$APP/Contents/"
file "$APP/Contents/MacOS/"*        # 架构 + 是否可执行
```

对照挂载卷内的原版比大小，确认不是拖拽不完整。

### 第 2 层：签名

```bash
/usr/bin/codesign -dv --verbose=4 "$APP" 2>&1 | head -20
/usr/bin/codesign --verify --deep --strict "$APP" 2>&1
```

- `Authority=Developer ID Application: <厂商>` → 正常分发
- `flags=0x10000(runtime)` → 硬化运行时已启用
- `valid on disk` + `satisfies its Designated Requirement` → 签名完好
- 无输出 = 校验通过

**app 内若有 `embedded.provisionprofile`，解析它**（用于判断分发类型与设备授权）：

```bash
/usr/bin/security cms -D -i "$APP/Contents/embedded.provisionprofile" 2>/dev/null \
  | plutil -p - | grep -E "Name|TeamIdentifier|application-identifier|ExpirationDate"
```

`ProvisionedDevices` 为空 = 企业/开发者签名，不限设备。若有设备列表且本机不在其中 → 启动必崩，无解，只能找发布方加设备。

**Entitlements**（判断 app 要什么权限、是否沙盒化）：

```bash
/usr/bin/codesign -d --entitlements :- "$APP" 2>/dev/null | plutil -p -
```

### 第 3 层：Gatekeeper 评估（**最关键的一层**）

```bash
/usr/sbin/spctl -a -vvv "$APP" 2>&1; echo "exit=$?"
```

> 注意路径是 `/usr/sbin/spctl`，**不是** `/usr/bin/spctl`（新版 macOS 上后者不存在）。

输出解读：

| spctl 输出 | 含义 | 处理 |
|---|---|---|
| `accepted` + `source=Notarized Developer ID` | 完全正常 | 问题不在 Gatekeeper，往下查启动层 |
| `rejected` + `source=no usable signature` | 签名缺失/损坏 | 重新下载 |
| **`File created by an AppSandbox, exec/open not allowed`** | **隔离属性异常**，Gatekeeper 拒绝 exec | 见第 4 层 |
| `rejected (the code is valid but does not seem to be an app)` | 不是合法 app bundle | 结构损坏 |

**必须在沙盒外复跑一次**确认结论（沙盒环境会干扰）：

```bash
/usr/sbin/spctl -a -vvv "$APP"     # 用 dangerouslyDisableSandbox=true
```

### 第 4 层：隔离属性（quarantine）—— 最高频根因

```bash
/usr/bin/xattr -p com.apple.quarantine "$APP"
/usr/bin/xattr -r -l "$APP" 2>/dev/null | grep -c quarantine   # 统计全 bundle 受影响文件数
```

格式：`flags;timestamp;AgentName;UUID`

- `AgentName` = 下载来源（Safari / Chrome / Quark / …）
- 正常 Safari 下载的 app：flags 形如 `01c3`
- **异常值（如 `0187`）会触发 `File created by an AppSandbox`** —— 常见于由自动化流程/沙盒进程安装的 app

**修复：**

```bash
# 1) bundle 根
/usr/bin/xattr -dr com.apple.quarantine "$APP"

# 2) 主可执行文件（关键！权限常为 r-xr-xr-x，xattr 删不掉）
/bin/chmod u+w "$APP/Contents/MacOS/<可执行文件名>"
/usr/bin/xattr -d com.apple.quarantine "$APP/Contents/MacOS/<可执行文件名>"

# 3) 全量清理（彻底，避免后续 Sparkle 自动更新再踩坑）
/bin/chmod -R u+w "$APP"
/usr/bin/xattr -dr com.apple.quarantine "$APP"
/usr/bin/xattr -r -l "$APP" 2>/dev/null | grep -c quarantine   # 期望为 0
```

**注意**：`chmod` 在 `/bin/chmod`，**不是** `/usr/bin/chmod`。`xattr` 在 `/usr/bin/xattr`。

**`chmod u+w` 不会破坏代码签名** —— 签名覆盖的是文件内容哈希，不含权限位。改完务必复跑 `codesign --verify` 确认。

### 第 4.5 层：来源标记（com.apple.provenance）—— 决定「能否执行」的第二把锁

`com.apple.provenance` 是 macOS 14+ 引入的属性，记录**创建该文件的进程**。它比 quarantine 隐蔽：`xattr -l` 只显示属性名、不显示值，必须用 `-px` 看十六进制。

```bash
exe="$APP/Contents/MacOS/$(/usr/bin/defaults read "$APP/Contents/Info.plist" CFBundleExecutable)"
/usr/bin/xattr -px com.apple.provenance "$exe" 2>&1
/usr/bin/xattr -l "$APP" 2>&1     # bundle 根，顺带看有无 com.apple.macl
```

**判定规则（本机 macOS 27 实测）**：

| quarantine | provenance | 结果 |
|---|---|---|
| 有 | 无 | ✅ 正常（手动从 dmg 拖拽安装的 app 都是这样） |
| 无 | 有 | ✅ 正常（应用自身自动更新时写入的） |
| 有（常规 flags 如 `03c1`） | 有 | ✅ 正常 |
| **有（异常 flags 如 `0187`）** | **有** | ❌ **`File created by an AppSandbox, exec/open not allowed`** |

**provenance 值相同 = 由同一个进程创建**，这是极强的溯源手段：

```bash
for a in /Applications/*.app; do
  exe="$a/Contents/MacOS/$(/usr/bin/defaults read "$a/Contents/Info.plist" CFBundleExecutable 2>/dev/null)"
  v=$(/usr/bin/xattr -px com.apple.provenance "$exe" 2>/dev/null | tr -d "\n")
  [ -n "$v" ] && printf "%-30s %s\n" "$(basename "$a")" "$v"
done
```

**根因判定**：若目标 app 的 provenance 值与某个**沙盒化的自动化工具**（AI agent、下载器、一键安装脚本）相同，说明它不是手动安装的，而是被该工具的沙盒进程写进 `/Applications` 的。macOS 因此拒绝执行它。

**处理**：清掉 quarantine 即可恢复（provenance 不必也不建议清除）。但下次安装同类 app 时，**改用「双击 dmg → 手动拖拽到 Applications」**，从源头避免。

**覆盖率判定（关键判据）**：统计 bundle 内带 provenance 的文件比例，可区分「整个 app 由程序释放」与「手动拖拽」：

```bash
tot=0; hit=0
while read f; do
  tot=$((tot+1))
  /usr/bin/xattr -p com.apple.provenance "$f" >/dev/null 2>&1 && hit=$((hit+1))
done < <(/usr/bin/find "$APP" -type f 2>/dev/null | head -300)
echo "$hit / $tot"
```

| 覆盖率 | 判定 |
|---|---|
| **接近 100%** | 整个 app 由某个程序**完整释放**进去（`ditto`/解压/复制），非 Finder 拖拽 |
| **0%** | 手动从 dmg 拖拽安装 |
| **部分** | 只有部分文件被改写 |

本机实测：Muse.app = `300/300`；OpenCode / Telegram / Obsidian / Figma = `0`。**Finder 拖拽不写 provenance** —— 这是区分两种安装方式的硬判据。

**注意**：排查时 `$APP/Contents/MacOS/$exe` 可能因 `defaults read` 取不到 `CFBundleExecutable` 而落空（表现为该 app 在对照脚本里被静默跳过）。此时直接 `ls "$APP/Contents/MacOS/"` 看真实可执行文件名。

### 第 5 层：实际启动

```bash
/usr/bin/open -a "$APP" 2>&1
sleep 8
pgrep -fl "<进程特征>" | head -5
ls -lt ~/Library/Logs/DiagnosticReports/ | grep -i "<关键词>" | head -3
```

- `open` 报 **`error -10810`** = LaunchServices 拒绝启动 → 基本就是第 4 层没清干净（尤其是主可执行文件的 xattr）
- 启动后无进程 + 有崩溃报告 → 读 `.ips` 报告定位
- 启动后无进程 + 无报告 + 无 stderr → 内核 exec 层被拒，回到第 3/4 层
- 可先用 `lsregister -f "$APP"` 刷新 LaunchServices 注册

```bash
/System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -f "$APP"
```

## 常见根因速查

| 现象 | 根因 | 解法 |
|---|---|---|
| 「已损坏，无法打开。应该将它移到废纸篓」 | quarantine 属性异常 | 第 4 层清理 |
| 「无法验证开发者」 | 未公证的 Developer ID | 第 4 层清理，或系统设置→隐私与安全性→仍要打开 |
| 「Apple 无法检查其是否包含恶意软件」 | 同上 | 同上 |
| `open` 返回 -10810 | 主可执行文件仍有 quarantine | 第 4 层第 2 步 |
| 双击图标跳一下就消失 | 架构不符 / 崩溃 | 第 1 层 `file` 查架构 + 第 5 层查崩溃报告 |
| Intel 版跑在 Apple Silicon | 缺 Rosetta | `softwareupdate --install-rosetta` |
| 启动即崩，无任何提示 | provisioning profile 不含本机 | 第 2 层解析 profile |
| 装好打不开，`spctl` 报 `File created by an AppSandbox` | 被沙盒化工具安装，带 provenance 标记 | 第 4.5 层 → 清理 quarantine |
| 同一个工具装的 app 有的能开有的不能 | 看 quarantine flags：`0187` 类异常值才触发 | 第 4.5 层对照表 |

## 本机（Eric / macOS 27 / Apple M5）实测结论

- `spctl` 只在 `/usr/sbin/spctl`；`chmod` 只在 `/bin/chmod`。
- `/Applications` 下 app 属主 `eric:admin`，owner 可 `chmod`，因此**不需要提权**即可完成全部修复。
- 直接运行 GUI app 的二进制（`"$APP/Contents/MacOS/Xxx"`）会被安全策略拦截，**不要用这个方式测试**，改用 `open -a`。
- 同机对照：Chrome 下载 app 的 quarantine flags 为 `03c1`/`01c1`，Safari 下载为 `01c3`/`0181`；`0187` 属异常值。
- 同机对照（provenance）：`/Applications` 下 30 个手动安装的 app **无** provenance；10 个带 provenance 的（Chrome/Brave/ChatGPT/Claude/Cursor/IINA/Lark/Steam/WeMD/WorkBuddy）全是**自带自动更新机制**或**由自动化工具安装**的。
- app 启动后常会自动 `hdiutil detach` 掉自己的安装卷，属正常行为。

## 收尾

修复后务必三连验证：

```bash
/usr/sbin/spctl -a -vvv "$APP"          # 期望 accepted
/usr/bin/codesign --verify "$APP"       # 期望 valid on disk
pgrep -fl "<进程特征>"                   # 期望有进程
```

并提醒用户：**若同一 app 之前下载过多次，不必重复下载**——问题在安装后的隔离属性，不在安装包。
