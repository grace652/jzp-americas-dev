#!/usr/bin/env bash
# 编译 OCR 工具（macOS 原生 Vision，无需安装任何依赖）
# 用法: bash build.sh [输出目录]
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUT="${1:-$HERE/build}"
mkdir -p "$OUT"

if ! command -v swiftc >/dev/null 2>&1; then
  echo "❌ 找不到 swiftc。请先装 Xcode Command Line Tools: xcode-select --install" >&2
  exit 1
fi

swiftc -O "$HERE/ocr.swift"     -o "$OUT/ocr"
swiftc -O "$HERE/ocrtext.swift" -o "$OUT/ocrtext"
echo "✅ 已编译: $OUT/ocr (纯文本)  $OUT/ocrtext (隐形文字层 PDF)"
