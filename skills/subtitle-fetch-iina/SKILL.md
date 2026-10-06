---
name: subtitle-fetch-iina
description: 为本地影视文件抓取高质量中文字幕并部署到 IINA 播放。当用户说「帮我找 XX 的字幕」「要质量好的字幕」「放到 IINA 里看」「字幕和视频对不上」「重新配字幕」时使用。覆盖 subhd.tv 搜索→下载直链→按内容识别版本→时间轴校验→部署命名（IINA 自动加载）的完整链路。
agent_created: true
---

# 字幕抓取与 IINA 部署

## 何时用

用户已有本地视频文件（.mkv/.mp4），需要中文字幕并在 IINA 中观看。

## 核心流程

### 1. 先摸清现场（不要跳过）

```bash
ls -d /Applications/IINA.app                      # IINA 是否安装
find ~/Movies ~/Downloads ~/Desktop -maxdepth 4 -iname "*<剧名>*"   # 找视频
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1 "<video>"  # 时长
```

**关键判断**：字幕的「片源版本」必须和视频的**发行组/介质**一致。
- 蓝光版（BluRay / REMUX / x264-ROVERS）和 HDTV 版的时间轴**通常相差 1～2 秒**，不能混用。
- 视频文件名里的 `BluRay` / `WEB-DL` / `HDTV` / `REMUX` 就是选字幕的依据。

### 2. 从 subhd.tv 搜索

```bash
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"
curl -s -A "$UA" "https://subhd.tv/search/<URL编码关键词>" -o s.html
```

- **站内 `/search/` 基本没用**（2026-09 实测）：无论中英文关键词，返回的都是一份固定热门榜，
  搜 `双峰` / `Twin Peaks` 都搜不到目标。**不要在这儿浪费时间**。
- **正确入口是直接猜/查豆瓣 ID 访问 `/d/<douban_id>`**——一次列出该剧全部字幕，中英文、各片源版本都在。
  - 豆瓣 ID 用 WebSearch 查（`<剧名> 豆瓣`），电影页 URL 里的数字即 ID。
  - 例：双峰第一季(1990) = `1295526`；猜错 ID 不会报错，只会返回别的片子，**务必核对返回的 `<title>`**。
  - 备用域名：`subhd.me` / `subhdtw.com`（主站 `subhd.tv` 可能有 Cloudflare 拦截页）。
- 条目链接形如 `/a/XXXXXX`（**短 ID，不是纯数字**），用正则 `href="(/a/[A-Za-z0-9]+)"` 提取。
- 条目字段顺序：`片源版本 · 来源类型 · 语言 · 格式 · 下载次数 · 上传人 · 日期`。
  优先「片源版本与视频发行组**逐字一致**」+ 语言含「双语」+ 格式 ASS。

### 3. 拿下载直链（两步 API，不需要登录）

```bash
# 第一步：进条目页拿会话 cookie，并 prepare-download
curl -s -A "$UA" -c cj.txt "https://subhd.tv/a/<SID>" -o /dev/null
curl -s -A "$UA" -b cj.txt -c cj.txt -H "Content-Type: application/json" \
     -H "Referer: https://subhd.tv/a/<SID>" -X POST -d '{"sid":"<SID>"}' \
     "https://subhd.tv/api/sub/prepare-download"
# → {"success":true,"url":"/down/<SID>"}

# 第二步：★必须先真访问一次 /down/<SID> 页面★，否则换不到地址
curl -s -A "$UA" -b cj.txt -c cj.txt "https://subhd.tv/down/<SID>" -o down.html
curl -s -A "$UA" -b cj.txt -c cj.txt -H "Content-Type: application/json" \
     -H "Referer: https://subhd.tv/down/<SID>" -X POST -d '{"sid":"<SID>"}' \
     "https://subhd.tv/api/sub/down"
# → {"success":true,"pass":true,"url":"https://dl.subhd.me/....zip"}
```

**两个必踩的坑（2026-09 实测）**：
1. **跳过 `/down/` 页面直接调 `/api/sub/down`** → 返回
   `{"success":false,"msg":"时间过长本临时页面已经失效"}`。
   `/down/` 页面必须先以 **GET** 访问一次（激活「临时页面」），再紧跟着调 API。
   curl `-o down.html` 是必需的，不要 `-o /dev/null` 省事。
2. 帖子里的 `/down/<SID>` 直链**只返回 HTML 中间页**，真实文件地址只在 `/api/sub/down` 的 JSON 里。

下载时带上 `-e "https://subhd.tv/down/<SID>"` 作为 Referer，并 `-L` 跟随跳转。

### 4. 解压（不一定需要 unrar，bsdtar 就够）

**macOS 自带 `/usr/bin/bsdtar` 原生支持 RAR 和 ZIP**，不必装 unrar/7z/unar：
```bash
bsdtar -xf pack_Q8DmxA.rar -C outdir/
```
要先 `mkdir -p outdir`。zip-in-zip / rar-in-zip 要展开两层。

zip 由 Windows 工具打包时中文文件名会被替换成 `?` 且重名覆盖，**必须逐个 entry 提取并用内容判定版本**：

```python
z = zipfile.ZipFile('pack.zip')
# 按 zip 内出现顺序映射到标准命名：
# 简体&英文.ass / 简体&英文.srt / 简体.ass / 简体.srt /
# 繁体&英文.ass / 繁体&英文.srt / 繁体.ass / 繁体.srt
```

编码顺序尝试：`utf-8-sig` → `utf-8` → `gb18030` → `big5` → `utf-16`。
判定繁简：统计 `来个们这说时对后发` vs `來個們這說時對後發`。
判定双语：`Dialogue:` 行里同时出现 CJK 和 `[A-Za-z]{3,}` 的比例。

**双语 ASS 的标准形态**（「官方字幕 中英+特效打磨」这类）：
- `[V4+ Styles]` 里同时定义 `Default`（中文）和 `eng`（英文）两个样式，中英是**两条按时间戳配对的 Dialogue 行**，
  不是一行内 `\N` 换行。
- **上中下英由 `MarginV` 决定，不用改任何东西**：`Default` 的 MarginV 大（如 83）、`eng` 的 MarginV 小（如 42），
  两者都是 `Align=2`（底部居中）→ 中文自然浮在英文上方。
- **若用户要的上下顺序反了**，只需对调两个 Style 的 `MarginV` 值即可，不必动 Dialogue 行。

### 4.2 ★双语包最常见的隐藏缺陷：中英不同起同落★

**「双语包」不等于「同步」。** 字幕组通常把中文按意群翻译（一句一屏），
英文沿用原片 CC/SDH 的切分（更碎、一句拆 2～3 屏）。结果：
中文的 `start` 和英文的 `start` 基本相同，但 **`end` 差很多** —— 英文先消失，中文还挂着。

**2026-09 实测**（Twin Peaks S01E01，喵千 官方双语 ASS）：887 条中文里有 **418 条（50%）**不同起同落，
典型如中文 `284.32→290.92` 对英文 `284.32→285.70`（英文早 5.2s 消失）。

**这是必查项**，交付前一定要量。度量方法（按屏幕实际观感，而不是比对首末时间）：
> 对每条中文窗 `[s,e]`，检查英文轨在 `s` 与 `e` 时刻是否都处于显示状态；
> 统计「英文晚出现」+「英文早消失」的条数占比。

**修复：合并到统一时间窗**（不能只把每对的时间戳拉齐，否则会串句）：
1. 取中文轨 + 英文轨**全部起止时间的并集**作为边界 grid
2. 相邻边界切成窗口；每个窗口取「覆盖该窗口」的当前中文行 / 英文行
3. 合并「中英文本都相同」的相邻窗口
4. 吸收 <0.6s 的碎片窗口到邻窗
5. 输出：每窗口写一条 `Default` + 一条 `eng`，**时间戳完全一致**

现成脚本：`scripts/merge_bilingual_ass.py`
```bash
python merge_bilingual_ass.py in.ass out.ass
# 输出：窗口 1309  中英配对 1160  仅中文 53  仅英文 96
```
Twin Peaks S01E01 修后：不匹配 **418 → 0**（配对率 60% → 92%）。
余下「仅中文/仅英文」窗口是**两轨内容本身不对应**（一轨有句、另一轨没有），
这类保持单语显示是正确行为，不必强行凑对。

**注意事项**：
- 脚本会**保留**头部 `[Script Info]`/`[V4+ Styles]` 原文与 `{\blur}`/`{\fade}` 等特效标签，
  以及 `note` 轨署名；仅重排 `Default`/`eng` 的时间戳。
- 改完**务必先备份原文件**（放 `字幕/原始未修正备份/`），再覆盖 IINA 自动加载的那份。
- 用户说「字幕一闪一闪」「中英不同步」「英文突然消失」时，先怀疑这个，不要先怀疑片源版本。

### 4.5 找不到现成双语包时的合成法

有些条目只有单语（如「Twin.Peaks.S01.1080p.BluRay.X264-REWARD 原创翻译」是简/繁 SRT）。
要得到双语就**合并两条已对齐的轴**：取该片的英文 `eng.srt` 与中文 `chs.srt`，
用 `scripts/merge_bilingual_ass.py` 的同款逻辑合并（先转成 ASS，中英各一行 Dialogue，
中文 MarginV 大、英文 MarginV 小）。
合成前**必须验证两条轴首末事件时间一致**，否则会串轴。
优先找现成双语包——**但现成双语包仍要查 4.2 的同步问题**。

### 4.7 ★字幕「位置太高」且用户说 IINA 设置里调不动★

**用户为什么调不动**：ASS 的 `MarginV` 是**硬编码在样式里**的。
IINA「设置 → 字幕」里的位置选项（`sub-pos`）主要作用于 SRT 等外挂纯文本字幕；
对 ASS/SSA，位置由样式决定，UI 里的滑块改动常常看不出效果甚至无效。
→ **要调 ASS 的位置，必须改文件里的 `MarginV`。**

**关键机制（容易搞错）**：
- `MarginV` = 该样式**文字块底边**距屏幕底边的距离（`Align=2` 底部对齐时）。
- **中文和英文是按各自的 `MarginV` 独立摆放的**，不是整体一块一起移动。
- 所以「让字幕更贴底」= **同时减小**两个 `MarginV`。
- **硬约束**：`中文MarginV ≥ 英文MarginV + 英文字高(≈字号×1.2)`，否则两行重叠。
  因为英文在下，中文不可能越过英文继续下移——**这是「下移」空间的真正上限**。

**算例**（Twin Peaks：中文59号/MarginV83，英文39号/MarginV42）：
- 英文行高 ≈ 39×1.2 = 47px → 中文底边至少 14(英文底)+47+间隙
- 英文 42→12，中文 83→64 已是较激进的下移；中文顶边从 14.2% 降到 12.5%
- 合计两行占屏幕 3.9%~14.2%，**本来就已经贴近底部**，可压缩余量只有 ~20px。
  用户若仍觉太高，通常是**字号偏大**导致的观感，而不是位置本身——这时要跟用户讲清这个约束，
  并给出「缩字号」的建议（用户可能像 Eric 一样明确表示不要改字号，那就照办并把余量用满）。

**操作脚本**：`scripts/adjust_ass_position.py`
```bash
python adjust_ass_position.py in.ass out.ass --cn-mv 64 --en-mv 12 [--cn-fs 48] [--en-fs 32]
```
只改 `Style:` 行的第 3 字段(字号)与 `MarginV`(第 22 字段)，**不碰任何 `Dialogue:` 行** →
时间轴与文字绝对安全。可用 `grep -c '^Dialogue:'` 前后对比自证。

**给用户的自助方案**（当用户会反复微调时值得做）：
在视频目录放一个 `调整字幕位置.command`（`chmod +x`），提示输入两个数字、
**从原始备份重新生成**（避免多次叠加修改），循环覆盖全季。
`.command` 双击即可在终端运行。注意脚本别依赖 `/tmp/venv_pdf`（重启会消失），用系统 `python3`。

**验收方式**：本机 ffmpeg **没有 libass**（`-h filter=subtitles` 报 Unknown filter），
无法烧录预览。只能靠：改完让用户看，并按用户反馈迭代。**先备份原样式**再改。

### 5. 时间轴校验（必做，否则可能白干）
用 ffprobe 取视频时长，再比字幕首末事件：

- 蓝光字幕末条事件通常落在 `片长 - 60~90 秒`（留片尾字幕），合理。
- **交叉验证法（最有说服力）**：拿一条**片源版本与视频逐字一致**的字幕，和候选字幕比同一句台词的起始时间。
  若首末事件几乎完全相同（如都从 `196.28s` 起、`5547.8s` 止），说明两者同轴，**可以直接用**。
  这比「算平均偏移量」快且可靠——真实字幕轴是**逐句手工微调**过的，偏移量并不恒定，
  用常数平移去「修」反而会破坏原轴。
- **画面对照法（终极确认）**：抽帧看画面 + 台词是否语义吻合。

```bash
ffmpeg -hide_banner -loglevel error -ss 88 -i "$V" -frames:v 1 -vf scale=800:-1 -y t.png
```
抽帧后用 Read 工具直接看图。**最佳锚点是「台词描述画面动作」的时刻**——
例：双峰 S01E01 在 223.09s 是 `雾笛又响了 / The lonesome foghorn blows.`，
抽帧可见 Pete 在湖边举着鱼竿、侧耳倾听 → 语义完全吻合，即证明轴是对的。
（片头标题卡也好用，但 90 年代老剧常常没有标题卡，别死等。）

### 5.5 先确认视频本身下载完了

字幕配好了但视频是半截的，白忙活。开播前查一下：

```bash
# 末尾 10 秒能否正常解码（半截文件会报 EBML / h264 错误）
ffmpeg -hide_banner -v error -sseof -10 -i "$V" -f null -
```

BT 下载中文件会持续变大，`stat -f%z` 隔几秒采两次即可估算速度。
**真实总大小**从种子文件里取（比瞎猜准）：

```python
# .torrent 是 bencode，用 files[].length 累加；注意有些种子是单文件用 info['length']
```

`.magent_*.torrent` / `.<视频名>.mkv.js` 这类隐藏文件说明下载器是 迅雷/magent 系的 BT 客户端。

### 6. 部署到 IINA

IINA/mpv 默认 `sub-auto=fuzzy`：**同目录下文件名以视频名（不含扩展名）开头的字幕会被自动加载**。

```
<视频目录>/
  true.detective.s01e01.1080p.bluray.x264-rovers.mkv
  true.detective.s01e01.1080p.bluray.x264-rovers.chs&eng.ass   ← 自动加载
  字幕/                                                        ← 备选版本，子目录不会被自动加载
    E01 简体&英文.srt
    E01 简体.ass
```

**只放一个**以视频名开头的字幕文件，否则多个会被一起加载造成叠字。备选版一律丢进子目录。

### 6.2 ★要同时提供「纯英文」等第二轨时★

用户常在看双语的同时想要一轨纯外文。**不要把第二轨放在视频同级目录** ——
IINA 默认 `sub-auto=fuzzy` 会把**所有**以视频名开头的字幕全部加载并叠加显示。

正确做法：
```
<视频目录>/
  twin.peaks.s01e01...mkv
  twin.peaks.s01e01...chs&eng.ass     ← 唯一自动加载（双语，默认轨）
  字幕/
    纯英文/E01 英文.srt               ← 第二轨放子目录，不自动加载
```
再配一个启动脚本按需指定（`.command` 双击运行，或用 `-e` 传集数）：
```bash
iina-cli --no-stdin "--sub-file=<英文.srt>" "--no-sub-auto" "<video.mkv>"
```
- **`--no-sub-auto` 是关键**：否则同级的双语 ASS 仍会被自动加载，与指定轨叠字。
- 切换轨也可让用户在播放中走 IINA 菜单「字幕 → 载入外部字幕」，无需重启。

**复用已有素材**：若 ZIP 里本来就带了 `English.PSA.srt/` 或 `*.eng.srt`，
直接拿它当纯英文轨，**不要再去下载**——它通常就是双语包英文轨的同一来源。

**注意**：若双语版做过「合并到统一时间窗」（见 4.2），
则其 `eng` 轨的行数/时间戳已与原始英文 SRT **不同**（英文被拆到多个窗口）。
原始 SRT 作为独立轨仍然正确（与视频同轴，可用片尾余量 60~90s 验证），
但**不要试图用它逐条对齐合并后的 ASS**，两者本就不该一致。

### 7. 启动

启动：

```bash
/Applications/IINA.app/Contents/MacOS/iina-cli --no-stdin \
  "--sub-file=/绝对/路径/xxx.ass" "/绝对/路径/video.mkv"
```

`iina-cli` 支持 `--mpv-<option>` 或裸 mpv 选项；默认启动后自身退出，加 `--keep-running` 可保持。

## 整季一次搞定

YYeTs 这类字幕组的剧集包是**整季打包**的（`S01E01`～`S01E08` 全在里面）。
第一次抓完就顺手把全季解出来放进 `字幕/` 子目录，后续用户再问「第 N 集字幕」时：

1. 直接 `ls 字幕/ | grep E0N`，**不用重新搜索下载**
2. 核对新一集视频的时长与字幕首末事件
3. 把 `E0N 简体&英文.ass` 复制成 `<视频名>.chs&eng.ass`
4. 开播

**校验锚点**：同一季各集的片名卡位置基本一致（True Detective S01 每集都在 ~86–90 s 出现 "TRUE DETECTIVE"），
比对该处画面即可快速确认字幕轴是否对得上，比逐句比对快得多。

## 坑

- **ASS 字体缺失**：字幕组的 ASS 常用 `方正黑体_GBK` / `微软雅黑` / `方正华隶_GBK`（macOS 都没有），
  libass 会回退到系统字体。**但若 ASS 里写的是 `Pingfang SC` / `Optima` / `Helvetica` 这类 macOS 原生字体，
  则完全无需担心**——先 `grep '^Style:'` 看一眼字体名再决定要不要提示用户。
  稳妥起见仍可另给一份同系列的 `.srt`（IINA 用自带样式渲染，干净可预测）。
- **本机 ffmpeg 可能没编 libass**（`ffmpeg -buildconf | grep ass` 为空），无法烧录 ASS 预览，别浪费时间。
  替代方案：抽帧看画面 + 人眼比对台词，足以验证对齐。
- `--sub-file` 路径含 `&` 时必须加引号（`"...chs&eng.ass"`），否则 shell 会把 `&` 当后台符号。
- 沙箱下 `ps` / `lsof` 可能被拒。确认 IINA 是否起来，用 `pgrep -f IINA`。
- 用户原有的 HDTV 字幕文件**不要删**，只提示时间轴对不上即可。
- **BT 正在下载的剧集**：先 `stat -f%z` 看每集大小，0 字节 / 几 MB 的是没下完的。
  字幕照常部署（不影响），但开播前明确指出**哪些集还不能看**，别让用户以为配好字幕就能播。
  `.magent_*.torrent`、`.<视频名>.mkv.js` 是迅雷/magent 系的 BT 临时文件，**不要当垃圾删掉**。
