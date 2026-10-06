---
name: pdf-shrink-for-email
description: 把体积过大的「纯图片型 PDF」（产品目录、画册、宣传册）压缩到可作邮件附件的体积，同时保证肉眼无差别。当用户说「PDF 太大发不了邮箱」「压缩一下 PDF」「这个目录/画册太重」「附件超限」「不影响画质的前提下压小」「PDF 瘦身」时使用。核心方法是先诊断体积构成（图片/文字/矢量），只有确认体积几乎全部来自全幅 JPEG 时才走重编码路线，并用 PSNR/SSIM 量化验证「视觉无损」。
agent_created: true
---

# 纯图片型 PDF 压缩（邮件附件）

## 目的

把过大的 PDF 压到能发邮件，且**肉眼看不出差别**。产出一到两个不同体积档位的文件，附带可量化的画质证据（PSNR/SSIM）。

## 何时使用 / 何时不要用

**先诊断，再动手。** 不要一上来就跑 Ghostscript 通用压缩。

| 诊断结果 | 走哪条路 |
|---|---|
| 体积 ≈ 全幅 JPEG 图像之和，无文字层、无矢量 | ✅ 本 skill：逐页 JPEG 重编码 |
| 有文字层/矢量 + 少量图片 | ❌ 本 skill 不适用。应回源文件重导出，或用 Ghostscript `/ebook`；盲目重编码会毁掉文字锐度 |
| 扫描件需要 OCR | ❌ 走 `scanned-pdf-ocr-macos` skill（那是加文字层，会变大不是变小） |

判断依据：`pdffonts` 字体数为 0、`get_text()` 为空、每页只有 1 张铺满整页的图。

## 关键洞察：为什么能压 60%

产品目录常由设计软件（InDesign/Canva/PDF24 等）以 **JPEG Q100** 导出，量化表 DC 全为 1，几乎没做量化——体积浪费极大。重编码到 Q90–92 时，**量化误差远小于人眼阈值**，但体积只剩三分之一。

实测（JZP 2026 目录，28 页 A4 横，206 DPI 全幅 JPEG，31.10 MB）：

| 档位 | 体积 | 体积比 | PSNR 均 | SSIM 均 | 判定 |
|---|---|---|---|---|---|
| 原始 | 31.10 MB | 100% | — | — | Q100 导出 |
| Q95 | 15.13 MB | 48.6% | 48.11 | 0.9999 | 视觉无损 |
| **Q92** | **11.88 MB** | **38.2%** | **46.52** | **0.9998** | **视觉无损，推荐** |
| Q90 | 10.91 MB | 35.1% | 45.69 | 0.9997 | 视觉无损 |
| Q85 | 8.94 MB | 28.7% | 44.05 | 0.9996 | 视觉无损 |
| 150 DPI + Q90 | 6.83 MB | 21.9% | 35.27 | 0.9940 | 屏幕无差别，打印偏软 |
| jpegtran 无损优化 | ~28 MB | ~90% | 无损 | 1.0000 | 真无损但省得太少，邮件不实用 |

**判定门槛**：PSNR ≥ 42 dB 且 SSIM ≥ 0.999 → 可称「视觉无损」；SSIM < 0.995 → 必须向用户明说这是「屏幕版」而非无损版。

## 标准流程

### 0. 环境

```bash
PY=/Users/eric/.workbuddy-ai/binaries/python/envs/default/bin/python
# 该 env 已装 pymupdf + pillow；缺则：
# $PY -m pip install pymupdf pillow
```

`/opt/homebrew/bin` 下系统自带 `jpegtran` / `cjpeg`（libjpeg-turbo），可用于真无损优化。

### 1. 诊断（必做，决定方案）

```bash
$PY scripts/pdf_probe.py "输入.pdf"
```

输出：页数、页面尺寸、每页图片数、图片格式/尺寸/占用、字体数、文本字符数、重复图片。**若字体数=0 且文本=0 且每页恰好 1 张图 → 确认走本 skill。**

### 2. 压一版试水并量化验证

```bash
$PY scripts/pdf_shrink.py "输入.pdf" "/tmp/try_q92.pdf" --quality 92
$PY scripts/pdf_verify.py "输入.pdf" "/tmp/try_q92.pdf"
```

看 PSNR/SSIM。达标再出正式版。

### 3. 出正式版（**绝不覆盖原文件**）

```bash
OUTDIR="<原文件所在目录>"
$PY scripts/pdf_shrink.py "输入.pdf" "$OUTDIR/NAME (Email Version).pdf" \
    --quality 92 --title "NAME"
$PY scripts/pdf_shrink.py "输入.pdf" "$OUTDIR/NAME (Email Version - Light).pdf" \
    --quality 90 --dpi 150 --title "NAME"
```

### 4. 人工目检（不能只信指标）

渲染原始 vs 压缩的同一区域做对比图，**用 Read 工具看图**确认：

- 挑**边缘密度最高**的页（通常是规格表、技术图纸）——最考验压缩
- 挑含**小字表格**的区域，300 DPI 渲染 + 1.5~2× 放大
- 挑**照片**区域看噪点/色带

`scripts/pdf_verify.py` 里已内置边缘密度排序，或直接：

```bash
$PY scripts/pdf_verify.py --visual "输入.pdf" "输出.pdf"
```

## 参数选择速查

| 需求 | 参数 |
|---|---|
| 邮件附件（推荐） | `--quality 92`，保持原 DPI |
| 更保险、可接受大一点 | `--quality 95` |
| 附件硬限制 10 MB 内 | `--quality 88` 或 `--dpi 170 --quality 90` |
| 只给屏幕看 / 手机 | `--dpi 150 --quality 90` |
| 需要真无损 | `jpegtran -progressive -optimize`（省 10%，邮件不实用） |

## 坑

- **不要降采样除非用户同意**。目录的原始 DPI 常是 200–300，降采样会毁掉打印质量。先只降 Q，不够再谈 DPI。
- **不要用 `-arithmetic`（jpegtran 算术编码）**。虽是无损且再省 5–9%，但部分 PDF 阅读器（尤其老版 Adobe、某些移动端）解不了算术编码 JPEG。
- **`brew install mozjpeg` 在本机被沙箱拦截**（`sandbox-exec: sandbox_apply: Operation not permitted`），别浪费时间；PyPI 也没有 `mozjpeg-lossless-optimizer`。libjpeg-turbo 的 Q92 已足够。
- **`qlmanage -t` 同样被沙箱拦截**，无法用 QuickLook 验证 PDF。改用 PyMuPDF 渲染 + `pypdf` 独立校验（页数/mediabox/是否加密）。
- **保持 4:2:0 子采样**（`--subsampling 2`）。若原图就是 4:2:0，改成 4:4:4 不会恢复已丢失的色度信息，只会让文件变大。
- **页数、页面尺寸、页序必须逐一核对**，用 `pdf_verify.py` 的「尺寸一致」列确认。
- **原文件一个字节都不要动**。只新增文件，同名冲突时加后缀。

## 交付时必须同时说明的两件事

1. **哪一档是给什么场景用的**，以及各自 PSNR/SSIM 证据。
2. **这份 PDF 有没有文字层**。纯图片型 PDF 不可搜索、不可复制文字——如果用户是要发给客户，值得提醒他根治方案是**回到设计源文件重导出矢量 PDF**，体积能降到 2–5 MB 且文字任意缩放都清晰。这是重编码永远达不到的。
