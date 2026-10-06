---
name: macos-power-sleep-control
description: 查询和修改 macOS 电源/睡眠行为。当用户说「插电会不会睡眠」「改熄屏时间」「屏幕多久关闭」「任务跑一半别让电脑睡」「合盖会不会断」「合盖还睡不睡」「防休眠」「显示器关闭时间」时使用。核心是先读 pmset 真实配置 + 日志取证，再把三件事分开讲：屏幕熄灭（displaysleep）、闲置系统睡眠（sleep）、合盖睡眠（Clamshell，只受 disablesleep 控制）。
agent_created: true
---

# macOS 电源与睡眠控制

## 何时用

用户问「会不会睡眠」「多久熄屏」「跑任务时别让电脑睡」「合盖会不会断」「改了设置为什么没生效」
「拔掉充电器屏幕就变暗」「电池模式下屏幕变暗怎么关」。
目标不是背参数，而是**先取证再改**，并且始终把三件事分开讲：

- **屏幕熄灭**（displaysleep）—— 只是背光关，系统照常跑
- **闲置系统睡眠**（sleep）—— 整机挂起，后台任务被暂停
- **合盖睡眠**（Clamshell）—— 硬件盖子触发，**只受 `disablesleep` 控制**，与 sleep 无关

用户说"熄屏"通常指第一件，说"任务不能断"要的是第二件不发生，说"合盖"问的是第三件。搞混就答错。

## 第一步：取证（不要凭记忆答）

```bash
pmset -g batt                      # 现在是用电池还是插电
pmset -g custom                    # 两套配置：Battery Power / AC Power
pmset -g                           # 关键：带"被谁阻止"的实时状态
pmset -g assertions                # 谁在持有防睡眠断言
```

原始配置文件（pmset -g custom 有时读缓存，以它为准）：

```bash
/usr/libexec/PlistBuddy -c "Print" /Library/Preferences/com.apple.PowerManagement.plist
```

字段对应关系：

| plist 字段 | pmset 输出 | 含义 |
|---|---|---|
| `Display Sleep Timer` | `displaysleep` | 无操作后关屏的分钟数，`0` = 永不 |
| `System Sleep Timer` | `sleep` | 无操作后整机睡眠的分钟数，`0` = 永不 |
| `Disk Sleep Timer` | `disksleep` | 硬盘休眠 |
| `Wake On LAN` | `womp` | 网络唤醒 |
| （plist 无此键） | `SleepDisabled` | `1` = 完全不睡，**连合盖也不睡**（全局总闸，慎用） |

## 第二步：日志取证（回答"实际会不会睡"）

配置说"允许睡"不等于"真的睡了"。用日志看实际行为：

```bash
pmset -g log | grep -E "Entering Sleep state|Wake from|Display is turned off|Display is turned on|Using AC|Using Batt" | tail -50
```

要点：
- 每条 `Entering Sleep state due to 'X'` 后面会跟 `Using Batt` / `Using AC`，**据此判断是哪套配置下真的睡了**。
- `due to 'Clamshell Sleep'` = 合盖导致的睡眠，**断言拦不住**。
- `due to 'Idle Sleep'` = 闲置超时睡眠，这个才是 displaysleep/sleep 控制的。
- 只看 `Assertions Summary` 行会漏掉真正的 Sleep 事件，务必把 Sleep/Wake 行一起 grep。

## 关键事实（Apple Silicon MacBook）

- **没有独立的"电脑睡眠"滑块**。系统设置里只有"若不活动则关闭显示器"（电池 / 电源适配器两档）。
- `System Sleep Timer` 出厂固定为 `1`，且**不代表真的等 1 分钟**。实测日志里屏幕熄灭到进入睡眠常常只隔几秒 —— 基本等于"屏幕灭了就睡"。
- **调低亮度 ≠ 不熄屏**。亮度调到 0 屏幕仍然会在计时到点后关闭，然后系统跟着睡。
- **合盖走独立通道**。没接外显时合盖会触发 `Clamshell Sleep`，**与 `sleep` 计时器完全无关** —— 把 `sleep` 设成 0 不影响合盖睡眠。详见下方专节。
- **第三方远程控制软件（UURemote / ToDesk / 向日葵等）会持有断言**，表现为"我明明设了熄屏它却一直亮"。查 `pmset -g assertions` 看 `PreventUserIdleDisplaySleep` 属于哪个 pid。
- `powerd` 持有 `Prevent sleep while display is on` 是**正常现象**，屏幕亮着时本来就不该睡，不用管。

## 合盖睡眠（Clamshell）—— 与闲置睡眠是两条独立通道

**最容易答错的一点：`sleep 0` 不会阻止合盖睡眠。**

| 触发方式 | 走哪条通道 | 谁能拦住 |
|---|---|---|
| 闲置超时（`Idle Sleep`） | `sleep` 计时器 | `sleep 0`、`caffeinate -i`、任何防睡眠断言 |
| 合盖（`Clamshell Sleep`） | 硬件盖子传感器 | **只有 `disablesleep` / `SleepDisabled`** |
| 苹果菜单 → 睡眠 | 用户主动 | 拦不住，也不该拦 |

由此得出一个高频需求的答案：**「插电开盖不睡、合盖照睡」只需要 `pmset -c sleep 0`，不需要额外做任何事。** 反过来，如果用户要「合盖也不睡」，那要动的是 `disablesleep` —— 全局总闸、副作用大，务必先确认用户真的要。

### 检测信号

```bash
# 合盖到底会不会睡 —— 最直接的信号
ioreg -r -k AppleClamshellState -d 4 | grep -E 'AppleClamshell(State|CausesSleep)'
#   "AppleClamshellCausesSleep" = Yes   → 合盖会睡（正常）
#   "AppleClamshellCausesSleep" = No    → 合盖不睡（异常，多半被 disablesleep 关了）
#   "AppleClamshellState" = Yes/No      → 当前盖子是否合着

# 全局总闸
pmset -g | awk '/^[[:space:]]*SleepDisabled[[:space:]]/{print $2; exit}'

# 是否接了外接显示器（接了 → 插电合盖进入「合盖模式」而不睡）
system_profiler SPDisplaysDataType -detailLevel mini | grep -c 'Connection Type: External'
```

注意 `ioreg` 输出的键名**带双引号**（`"AppleClamshellCausesSleep" = Yes`），取值要用 `sed -n 's/.*= *//p' | tr -d '"'`。`system_profiler -detailLevel mini` 实测约 0.16s，可以接受。`SleepDisabled` 必须从 `pmset -g` 读，plist 里没有这个键。

Apple Silicon 上的「合盖模式」（插电合盖不睡）需**同时满足**：接电源 + 外接显示器 + 外接键鼠。缺一不可，且是系统设计，无法用 pmset 关闭。

## 第三步：改设置

### 改熄屏时间（按供电状态分开设）

`-b` = 电池，`-c` = 插电，`-a` = 两者。

```bash
sudo pmset -b displaysleep 15    # 电池：15 分钟不操作熄屏
sudo pmset -c displaysleep 10    # 插电：10 分钟
sudo pmset -b sleep 0            # 电池：永不整机睡眠（一般不推荐，费电）
sudo pmset -c sleep 0            # 插电：永不整机睡眠（长时间跑任务推荐）
```

### 关闭「拔电源后屏幕自动变暗」（lessbright）

**症状**：拔掉充电器后屏幕立刻暗一档；插回去又亮回来。这是 `lessbright`，**不是自动亮度**。

该字段**只出现在 `Battery Power` 段**，AC 段没有这个键：

- `1` = 电池供电时把屏幕轻微调暗一档（**出厂默认**）
- `0` = 不变暗

**系统设置里没有这个开关**，只能走 pmset。

```bash
# 取证
pmset -g custom | sed -n '/Battery Power/,/AC Power/p' | grep lessbright

# 关闭（本机沙箱内 sudo 不可用，必须走 osascript 提权）
osascript -e 'do shell script "/usr/bin/pmset -b lessbright 0" with administrator privileges'

# 恢复出厂默认
osascript -e 'do shell script "/usr/bin/pmset -b lessbright 1" with administrator privileges'
```

**易混淆项与排查顺序**（症状像，触发条件不同）：

| 触发条件 | 设置项 | 在哪改 |
|---|---|---|
| **插拔电源**瞬间变暗 | `lessbright` | 只能 pmset，**无 GUI 开关** |
| 环境光变化（开灯 / 拉窗帘） | 自动调节亮度 | 系统设置 → 显示器 |
| 电量低到阈值后变暗降频 | `lowpowermode` | 系统设置 → 电池 → 低电量模式 |

先确认触发条件是「插拔电源」还是「环境光变化」，再决定动哪个 —— 选错会改了没效果。

实测（eric / Apple M5 / macOS 27）：出厂 `lessbright 1`，`pmset -b lessbright 0` 后回读确认生效。

### 自动亮度偏暗怎么办（结论：官方范围内无解）

**症状**：开启「自动调节亮度」后屏幕比期望的暗；手动拖滑块能到更高亮度。

**根因**：自动亮度是 `ALS 读数 → 私有映射曲线 → 背光`，曲线输出值域被**刻意收窄**（给极端强光留 headroom）。
手动拖动只是**临时覆盖**，环境光一变系统就重新接管 —— 所以"手动能到 100%、自动到不了"。

**查证结论（eric / macOS 27 / Apple M5，2026-09-26）**：该曲线**没有公开配置接口**：

| 检查对象 | 结果 |
|---|---|
| `com.apple.CoreBrightness` 偏好域 | **不存在** |
| `~/Library/Preferences/ByHost/` | 无亮度相关 plist |
| `com.apple.BezelServices.plist` | 存在但内容为空（Apple Silicon 已弃用） |

→ 状态由 CoreBrightness / DisplayServices 私有框架管理，**只能 GUI 或私有 API 访问**，
不能用 `defaults` / plist 调高。

**官方范围内可做的三件事**：
1. **排查 ALS 遮挡**（唯一可能让自动亮度恢复正常的项）：摄像头隐私贴纸、覆盖上边框的屏幕膜、保护壳/键盘膜边缘 —— 读数被压低 → 系统误判"环境很暗" → 亮度偏低
2. 关夜览 / 原彩显示：不改背光，但改善"显暗"观感
3. 要可控亮度就**保持自动关闭**，用 F1/F2 手动设，值跨重启保持

**第三方工具的能力边界**（供回答用户提问时判断，**不要主动推荐**）：

| 工具 | 能力 | 限制 |
|---|---|---|
| **Lumos**（免费开源 MIT） | 私有 `DisplayServicesSetBrightness` 控内置屏；从手动修正中学习曲线 | 按**屏幕内容**自适应（非环境光）；须关系统自动亮度；需屏幕录制权限 |
| **Lunar Pro**（$23） | Sensor Mode 在 Apple Silicon 可读内置 ALS；曲线可学习 | 官方定位是**外接显示器**，"内置屏可否作为控制目标"**未明确**，效果不确定 |

**⚠️ 用户偏好**：Eric 明确坚持只用 Apple 官方方案，不接受第三方工具。
遇到系统限制时**先如实说明官方边界**，再给官方范围内的可选项，不要默认推荐装工具。

### 权限：sandbox 里 sudo 不可用

直接 `sudo` 会被沙箱拒绝（`operation not permitted`）。**用 osascript 走系统授权弹窗**，用户点一下密码即可：

```bash
osascript -e 'do shell script "/usr/bin/pmset -c sleep 0" with administrator privileges'
```

需要 `dangerouslyDisableSandbox: true`，否则弹窗起不来。

### 临时防睡眠（不改配置，任务结束自动释放）

```bash
caffeinate -is        # -i 阻止闲置睡眠，-s 阻止插电睡眠；屏幕仍可正常熄灭
```

标志位速查：

| 标志 | 作用 | 是否影响屏幕 |
|---|---|---|
| `-d` | 阻止屏幕熄灭 | 屏幕常亮 |
| `-i` | 阻止闲置系统睡眠 | 屏幕可正常熄灭 ✅ |
| `-s` | 阻止系统睡眠（仅插电生效） | 屏幕可正常熄灭 ✅ |
| `-m` | 阻止硬盘休眠 | — |
| `-t N` | N 秒后自动退出 | — |

"跑任务、屏幕可以灭"→ 用 `caffeinate -is`，**不要加 `-d`**。

### ⚠️ caffeinate 在这个环境里活不过一次会话

**实测结论（务必记住）：`nohup ... & disown` 不起作用。** 后台起的 `caffeinate` 会在当前轮次/会话结束时被回收，`pgrep` 再查就是空的。`launchctl submit` 在沙箱内也直接返回 exit=1。

所以：

- **要跨会话生效的防睡眠，只能用 `pmset`**（无进程，写进系统配置）。
- `caffeinate` 只适合"当次命令内"的短时保护，或者由用户**在自己的 Terminal 窗口里**手动跑。
- 不要向用户承诺"已经挂了个后台进程兜底"——先 `pgrep` 复查，再说话。

验证 caffeinate 是否还活着（每次声称之前都跑一次）：

```bash
pgrep -fl caffeinate || echo "已消失"
```

## 第四步：验证（必须做）

改完必须回读，不要相信命令的 exit code：

```bash
pmset -g custom | sed -n '/AC Power/,$p'
pmset -g          # 会显示 "sleep 0 (sleep prevented by ...)" 这类实时状态
```

注意：`PlistBuddy -c "Print"` 可能返回**缓存值**。本次实测 `pmset -c sleep 0` 后 PlistBuddy 仍显示 `System Sleep Timer = 1`，但 `pmset -g custom` 已正确显示 `sleep 0`。**以 pmset 输出为准。**

解析坑：`pmset -g` 输出的这些行**行首带前导空格**，用 `^sleep` 会一条都匹配不到。正确写法：

```bash
pmset -g | grep -E "^[[:space:]]*(sleep|displaysleep)[[:space:]]"
pmset -g custom | sed -n '/^AC Power:/,$p' | awk '$0 ~ "^[[:space:]]*sleep[[:space:]]" {print $2}'
```

用 `awk` 精确取字段时注意 `sleep` 的前缀匹配会误伤 `displaysleep` —— 靠 `^[[:space:]]*sleep[[:space:]]` 里的尾部空格把它排除掉（`displaysleep` 后面是空格没错，但 `sleep` 前面是 `y` 不是空白，所以安全）。`Sleep On Power Button` 因首字母大写不会被匹配。

## 交付方式：做成开关脚本，别只给命令

用户记不住 pmset 参数。**把 on / off / status 封装成一个 bash 脚本，再配几个 `.command` 双击入口**（macOS 双击 `.command` 会直接用终端跑）。这样用户平时只双击，不用碰命令行。

约定：

- 脚本放工作区自己的目录（如 `<工作区>/keepawake/`），不要写进 `~/.workbuddy-ai/`。
- `status` 做成默认动作，且**要包含体检而不只是报数字** —— 判断"是否符合用户预期"，异常项打 `✗` 并给出修复命令。
- 提权统一走 `run_root()` 包装 `osascript -e 'do shell script "..." with administrator privileges'`，脚本里不要直接 `sudo`（沙箱会拒）。
- `.command` 文件首行 `cd "$(dirname "$0")"`，末尾 `read -r _` 防止窗口闪退。
- 改完必须 `bash -n` 逐个语法检查，再实跑一次 `status` 验证输出。

## 回滚

改完记得告诉用户怎么恢复，并给出可直接粘贴的命令：

```bash
osascript -e 'do shell script "/usr/bin/pmset -c sleep 1" with administrator privileges'
pkill caffeinate    # 仅当确实用过 caffeinate 时才需要
```
