---
name: scanned-pdf-ocr-macos
description: 在 macOS 上给扫描件 PDF 做 OCR，产出可搜索 PDF（原图 + 隐形文字层）与纯文本，无需安装 tesseract/pyobjc。当用户说「PDF 读不出内容」「NotebookLM/ChatGPT 读不到这个 PDF」「扫描件识别」「OCR」「可搜索 PDF」「PDF 没有文字层」「拖选不了文字」「图片型 PDF 转文字」时使用。也适用于把扫描的合同、书、手册变成可检索、可喂给 LLM 的文本。
agent_created: true
---

# 扫描件 PDF OCR（macOS 原生）

## 目的

把**没有文字层**的 PDF（扫描件、拍照件、传真件）转成可检索、可喂给 LLM 的形态。产出两样：

1. **可搜索 PDF** —— 保留原页面图像，叠加一层不可见的文字层。视觉不变，但能选中、能搜索、NotebookLM 等工具能读、引用能锚定到真实页码。
2. **纯文本 / Markdown** —— 用于直接喂给 LLM 或做知识库蒸馏。

## 何时使用

先判断是不是扫描件。**5 秒自检法**：在 PDF 里拖选一句话，选不中就说明没有文字层。程序化判断：

```bash
python -c "
from pypdf import PdfReader
r = PdfReader('x.pdf')
t = sum(len((p.extract_text() or '').strip()) for p in r.pages[:5])
print('前5页可提取字符:', t, '→', '扫描件' if t < 100 else '有文字层')
"
```

若「扫描件」成立，走本 skill。

**⚠️ 判据会被水印骗过，不要只看前 3 页。** 有些扫描件每页带几百字水印（如「米课内部资料」重复 202 字/页），前 3 页字符数会很高，但正文一个字都提取不到。必须：抽样 **10–12 页**、**去水印后**再统计，或抽查每页的嵌入图像数量（扫描件几乎每页都有 1 张大图）。

```bash
python -c "
import re
from pypdf import PdfReader
WM = re.compile(r'米课内部资料|hxg3366|本人外贸|ice\.imiker|内部资料')
r = PdfReader('x.pdf'); n = len(r.pages)
probe = list(range(0, n, max(1, n//12)))[:12]
real = sum(len(WM.sub('', re.sub(r'\s','', r.pages[i].extract_text() or ''))) for i in probe)
print(f'{n} 页，去水印后 {real/len(probe):.0f} 字符/页 →', '扫描件' if real/len(probe) < 30 else '有文字层')
"
```

## 为什么不用常见方案

- `tesseract` / `pyobjc` / `pytesseract` / `ocrmypdf`：多数 Mac 上没装，且 `brew` 可能也没有。
- macOS **自带 Vision 框架**，中英混排识别质量优于 tesseract，且**零安装**。只需 `swiftc`（Xcode Command Line Tools，`/usr/bin/swiftc`）。

先确认环境：

```bash
command -v swiftc || echo "缺 CLT，需 xcode-select --install"
```

## 执行流程

### 1. 编译工具

```bash
bash scripts/build.sh /tmp/ocrbin
```

产出 `/tmp/ocrbin/ocr`（纯文本）与 `/tmp/ocrbin/ocrtext`（隐形文字层 PDF）。

### 2. 抽纯文本

```bash
/tmp/ocrbin/ocr input.pdf > out.txt          # 全书
/tmp/ocrbin/ocr input.pdf 20 60 > out.txt    # 只跑第 20–60 页（先小样验证）
```

输出以 `===== PAGE n =====` 分页。**先跑 3–5 页确认质量再跑全书。**

### 3. 生成可搜索 PDF

两步走，顺序不能颠倒：

```bash
# ① 生成体积很小的隐形文字层（300 页约 1MB）
/tmp/ocrbin/ocrtext input.pdf layer.pdf

# ② 叠加回原书 + 三重校验（用项目自己的 venv 跑）
python scripts/make_searchable.py input.pdf layer.pdf output.pdf
```

`make_searchable.py` 会校验三件事，任一项不过就报错退出：页数一致、文字层确实生效（可提取字符数 > 1000）、**抽样页面的嵌入图像 MD5 与原书一致**（确保没破坏画面）。

### 4. 清洗文本（可选）

OCR 结果常带三类噪声，按需正则清理：

| 噪声 | 处理 |
|---|---|
| 卖家水印（微信号、二维码文案、网站域名） | 整行删除 |
| 重复的书名页眉/页脚 | 整行删除，或改写成 markdown 标题 |
| 纯页码行 | 删除，页码改用 `<!-- p.N -->` 注释保留 |

页码务必保留 —— 下游引用、校对都要靠它。若 PDF 页码与书内印刷页码有偏移，在文件头注明换算关系。

## 关键坑（都已踩过，不要再走）

1. **不要在 CGContext 里重新渲染页面图像来合成可搜索 PDF。** 渲染成 2000px 宽位图后写入 PDF 是未压缩的，实测 **1.9MB/页**，300 页会到 500MB+。必须走「只生成文字层 + pikepdf 叠加」，同样 300 页只有 21MB。
2. **隐形文字的字体必须支持中文。** 用 `PingFangSC-Regular`（或 `STHeiti`）。用 Helvetica 之类会导致 CJK 落成 `.notdef`，文字层提取出乱码。文字用 `ctx.setTextDrawingMode(.invisible)` 绘制。
3. **`pypdf` 解不了有打开密码的 PDF**（会抛 `FileNotDecryptedError`），要解密得用 `pikepdf.open(path, password=...)`。而「仅有 owner 限制、空密码」的文件 `pypdf` 能直接读。
4. **扫描件的页面图像指纹不能用来切分章节。** 尝试用页眉的 MD5 或水平投影差分检测章节边界会失败 —— 扫描噪声加上奇偶页的细微差异，会让每页都被判成变化点。要还原章节结构，改用人眼读几张页眉图（用 PIL 裁页眉条横向拼接成网格再读），别做自动指纹。
5. **OCR 会漏字符但不会报错。** 一定要抽查：统计每页字符数，把明显偏薄的页挑出来，导出原图人工比对，确认是「书上本来留白」还是「识别失败」。
6. **阅读顺序可能错位。** 信件类、多栏类版面的行序偶尔会被打乱。对顺序敏感的内容（如范文）要人工顺一遍。

## 质量预期

实测一本 298 页、943×1363 扫描的中文书：

- 耗时：OCR **75 秒**，叠加 **< 1 秒**
- 产出：可提取正文 17.3 万字符，276/298 页有实质内容
- 体积：原书 20.3MB → 可搜索版 21.1MB
- 典型错字：形近字（来→米、梯→样、欧→吹）；页眉偶被读乱

结论：**够用，但引用关键数字（金额、日期、比例、标准号）前要核对原图。**

## 批量处理

多个扫描件时逐个走同一流程即可。OCR 是 CPU 密集的单进程任务，串行跑即可，不必并行。

**先做全目录体检，再决定 OCR 谁** —— 别等逐个上传失败才发现。写一个循环，对每个 PDF 抽样 10–12 页（跨全书均匀取样），统计**去水印后**的可提取正文字符数与含嵌入图像的页数：

```python
# 判据：正文 < 30 字符/页 且 绝大多数页含大图 → 扫描件
probe = list(range(0, n, max(1, n // 12)))[:12]
real = sum(len(WM.sub("", re.sub(r"\s", "", r.pages[i].extract_text() or ""))) for i in probe)
```

水印正则参考：`米课内部资料|hxg3366|本人外贸\s*14\s*年|更多外贸课程资料|ice\.imiker|www\.[a-z0-9\-]+\.(com|cn)`

**实测性能**：1019 页共约 9 分钟（约 2 页/秒），叠加文字层近乎瞬时。

## 上传目标平台的限制（NotebookLM / Gemini Notebook）

2026-07-16 起 NotebookLM 已改名 **Gemini Notebook**。单份 source 上限 **50 万词或 200MB**（免费版每 notebook 50 份 source）。

**优先交付纯文本 md，而不是可搜索 PDF** —— 体积小两个数量级、无 OCR 层怪癖、更适合喂提示词。可搜索 PDF 只在需要**页码锚定引用**时才用。

## 交付前自检

- [ ] 已用 5 秒自检法或字符统计确认原文件确实无文字层
- [ ] 先小样验证过 OCR 质量，再跑全书
- [ ] 可搜索 PDF 的三重校验全部通过
- [ ] 抽样翻页确认画面未被破坏
- [ ] 文本已清洗水印，且页码标记保留
- [ ] 把「偏薄页」清单核对过，确认不是识别失败
