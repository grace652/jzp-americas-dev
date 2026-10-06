#!/usr/bin/env python3
"""Stage 6 - design the on-cover text from an article.

The hard editorial problem: a WeChat / YouTube title is a SENTENCE
("三十岁之前必看的防内耗指南"), but a cover headline is a CONCEPT
("内耗"). This script bridges that gap mechanically, then leaves the final
taste call to a human or the agent.

It segments the title and body with jieba, builds word-level candidates
(single content words plus adjacent noun compounds), and scores them against
the qualities that make a cover headline work:

    concrete > abstract      "人生大坑" beats "决策陷阱"
    tension  > neutrality    "内耗" beats "成长"
    concept  > sentence      "男性困境" beats "为什么现代男性..."

and penalises the classic traps (list markers, question particles, function
words, non-words).

Traditional Chinese input is converted to Simplified first, since the output
must be Simplified.

This is a candidate generator, not an oracle. Read the ranked list, then pick.

Usage:
    python 07_design_text.py --title "三十岁之前必看的防内耗指南"
    python 07_design_text.py --title "..." --body article.md
    python 07_design_text.py --url "https://mp.weixin.qq.com/s/xxxx"
    python 07_design_text.py --title "..." --body article.md --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore", category=SyntaxWarning)

CJK = r"\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff"
CJK_RE = re.compile(f"[{CJK}]")

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

try:
    import jieba
    import jieba.posseg as pseg
    _JIEBA = True
except ImportError:  # pragma: no cover
    _JIEBA = False

try:
    import opencc
    _CC = opencc.OpenCC("t2s")
except Exception:  # noqa: BLE001 - optional
    _CC = None


# --------------------------------------------------------------------------- #
# lexicons
# --------------------------------------------------------------------------- #
# Words that carry a picture. A headline containing one of these is far more
# memorable than a purely abstract one.
CONCRETE = set(
    "坑 洞 门 墙 锁 刀 火 冰 山 海 路 桥 网 绳索 根 果 刺 伤口 疤 毒 药 梦 影 风 "
    "浪 潮 岸 崖 谷 林 雾 镜子 窗 房 顶 地板 翅膀 枷锁 牢笼 面具 壳 罐 盒子 钉子 "
    "锤子 火焰 冷水 沙 石子 石头 树木 叶子 花瓣 种子 土壤 井 隧道 黑洞 悬崖 漩涡 "
    "齿轮 杠杆 支点 砝码 天平 闸门 开关 按钮 屏幕 信号 天线 罗盘 地图 航线 灯塔 "
    "锚 桅杆 船 桨 车轮 轨道 站台 迷宫 荒原 沙漠 孤岛 围墙 高墙 深渊 陷阱 牢 狱".split()
)

# Words that name a felt problem or a charged state. These create tension.
TENSION = set(
    "内耗 焦虑 困境 迷茫 孤独 恐惧 愤怒 羞耻 后悔 拖延 逃避 讨好 比较 嫉妒 失败 "
    "崩溃 疲惫 空虚 浮躁 执念 控制 依赖 边界 自尊 价值 意义 自由 选择 代价 陷阱 "
    "误区 谎言 真相 痛苦 压力 倦怠 麻木 内疚 自责 内卷 躺平 攀比 自卑 傲慢 虚荣 "
    "执迷 上瘾 崩塌 瓦解 分裂 撕裂 缝隙 失衡 错位 落差 亏欠 遗憾 纠结 挣扎 沉沦 "
    "消耗 贫穷 匮乏 稀缺 过剩 浪费 噪音 干扰 阻力 惯性 强迫 绑架 勒索 剥夺 "
    "沉默 妥协 委屈 憋屈 压抑 内伤 反噬 恶果 瓶颈 天花板 死循环 无底洞".split()
)

# Positive concepts: the "promise" side of the ledger. The reference channel
# uses these too (希望), so they deserve their own credit rather than being
# lumped in with tension words.
PROMISE = set(
    "希望 勇气 信任 亲密 接纳 原谅 成长 改变 坚持 放下 释怀 和解 自由 清醒 专注 "
    "自律 掌控 边界 底气 松弛 从容 热爱 意义 方向 答案 出口 转机 破局 复利 "
    "耐心 定力 分寸 格局 视野 洞察 觉醒 顿悟 重建 修复 复原 韧性 内核 底色".split()
)

# Morphemes that mark a noun phrase rather than a verb phrase or sentence.
NOMINAL_SUFFIX = (
    "力", "感", "症", "学", "主义", "思维", "模式", "关系", "状态", "问题",
    "法则", "原理", "逻辑", "系统", "结构", "机制", "现象", "本质", "规律",
    "密码", "答案", "起点", "终点", "出口", "入口", "边界", "底线", "习惯",
    "代价", "成本", "周期", "阶段", "过程", "结果",
)

# Pure filler: never a good headline on its own.
STOPWORDS = set(
    "我们 你们 他们 她们 它们 自己 这个 那个 这些 那些 什么 怎么 为什么 如何 "
    "因为 所以 但是 而且 如果 虽然 可以 可能 应该 需要 必须 已经 正在 还有 没有 "
    "不是 就是 一样 一些 非常 特别 今天 明天 昨天 现在 时候 时间 事情 东西 地方 "
    "人们 大家 朋友 方式 方法 情况 这种 那种 以及 并且 然后 其实 真的 视频 文章 "
    "内容 分享 聊聊 说说 看看 想想 知道 了解 一个 两个 三个".split()
)

# POS tags that make a good headline
GOOD_POS = {"n", "nr", "ns", "nt", "nz", "ng", "vn", "an", "a", "i", "l", "j"}
BAD_POS = {"r", "c", "p", "u", "uj", "ul", "uz", "d", "m", "mq", "q", "f", "t",
           "xc", "w", "e", "o", "y", "zg", "x"}

LIST_RE = re.compile(
    r"^[一二三四五六七八九十两0-9]+\s*(个|种|条|件|点|步|招|类|大|方面|方法|建议|"
    r"信号|决定|习惯|误区|陷阱|难题|困境|原因|信号)"
)
QUESTION_TAIL_RE = re.compile(r"[吗呢吧么]$")
# Generic title furniture. A compound ending in one of these is a title
# fragment, not a cover concept ("内耗指南" is worse than "内耗").
GENERIC_SUFFIX = (
    "指南", "手册", "攻略", "方法", "建议", "清单", "盘点", "总结", "分享",
    "揭秘", "笔记", "心得", "教程", "全解", "详解", "真相", "秘密",
)
TITLE_TAIL_RE = re.compile(
    r"(指南|手册|攻略|方法|建议|清单|盘点|总结|分享|揭秘|真相|秘密|笔记|心得|"
    r"是什么|怎么办|为什么|怎么|如何|的|之前|之后|必看|必读)$"
)
# "EP26." / "第 26 集" / "26、" style episode prefixes
EPISODE_PREFIX_RE = re.compile(r"^\s*(?:EP|Ep|ep|第)?\s*\d+\s*(?:集|期|话)?\s*[.、:：\-—]?\s*")


# --------------------------------------------------------------------------- #
# text input
# --------------------------------------------------------------------------- #
def to_simplified(text: str) -> str:
    return _CC.convert(text) if _CC else text


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?is)<br\s*/?>|</p>|</div>|</h[1-6]>", "\n", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    for a, b in (("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"),
                 ("&quot;", '"'), ("&#39;", "'"), ("&mdash;", "—"), ("&ldquo;", "“"),
                 ("&rdquo;", "”"), ("&hellip;", "…")):
        text = text.replace(a, b)
    text = re.sub(r"[ \t\u3000]+", " ", text)
    return re.sub(r"\n{2,}", "\n", text).strip()


def fetch_article(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=40) as resp:
        raw = resp.read()
    for enc in ("utf-8", "gbk", "gb18030"):
        try:
            return strip_html(raw.decode(enc))
        except UnicodeDecodeError:
            continue
    return strip_html(raw.decode("utf-8", errors="ignore"))


# --------------------------------------------------------------------------- #
# candidate extraction
# --------------------------------------------------------------------------- #
def tag(text: str) -> list[tuple[str, str]]:
    """[(word, pos)] - jieba if available, else a crude CJK-run fallback."""
    if _JIEBA:
        return [(w.word, w.flag) for w in pseg.cut(text) if w.word.strip()]
    return [(m.group(0), "n") for m in re.finditer(f"[{CJK}]+", text)]


def content_words(text: str) -> list[tuple[str, str]]:
    return [
        (w, p) for w, p in tag(text)
        if CJK_RE.search(w) and p not in BAD_POS and w not in STOPWORDS
    ]


def morpheme_hits(word: str, lexicon: set[str]) -> list[str]:
    """Exact word match, or a lexicon entry contained in the word."""
    if word in lexicon:
        return [word]
    return [m for m in lexicon if len(m) >= 2 and m in word]


def score_candidate(word: str, pos: str, in_title: bool, in_lead: bool,
                    freq: int) -> tuple[float, list[str]]:
    reasons: list[str] = []

    if word in STOPWORDS or len(word) < 2 or len(word) > 4:
        return -999, ["长度或虚词不合格"]
    if LIST_RE.search(word):
        return -60, ["列表标记词（三个/六种/五大），封面不合适"]
    if QUESTION_TAIL_RE.search(word):
        return -30, ["疑问语气词结尾"]
    if not CJK_RE.search(word):
        return -999, ["非中文"]
    if pos in BAD_POS:
        return -40, [f"词性不适合做标题（{pos}）"]

    score = {2: 2.0, 3: 2.6, 4: 3.0}.get(len(word), 0.0)

    # a compound ending in generic title furniture is a title fragment
    if len(word) > 2 and any(word.endswith(s) for s in GENERIC_SUFFIX):
        score -= 4.5
        reasons.append("以泛用词收尾（指南/方法类），是标题碎片")

    tension = morpheme_hits(word, TENSION)
    if tension:
        score += 4.0 if word in TENSION else 3.0
        reasons.append(f"冲突/情绪：{'/'.join(tension[:3])}")

    promise = morpheme_hits(word, PROMISE)
    if promise:
        score += 3.8 if word in PROMISE else 2.6
        reasons.append(f"正向概念：{'/'.join(promise[:3])}")

    concrete = morpheme_hits(word, CONCRETE)
    if concrete:
        score += 3.4 if word in CONCRETE else 2.4
        reasons.append(f"具象：{'/'.join(concrete[:3])}")

    if any(word.endswith(s) for s in NOMINAL_SUFFIX):
        score += 1.6
        reasons.append("名词性收尾")

    if pos in ("n", "nr", "ns", "nt", "nz", "ng"):
        score += 2.2
        reasons.append("名词")
    elif pos in ("vn", "an"):
        score += 1.6
        reasons.append("动名词")
    elif pos == "a":
        score += 0.8
    elif pos == "v":
        score += 0.4

    if in_title:
        score += 3.4
        reasons.append("出现在标题")
    if in_lead:
        score += 1.4
        reasons.append("出现在开篇")
    if freq > 1:
        score += min(1.6, 0.4 * freq)
        reasons.append(f"正文出现 {freq} 次")

    if not tension and not concrete and not promise and not any(
        word.endswith(s) for s in NOMINAL_SUFFIX
    ):
        score -= 2.0
        reasons.append("偏抽象")

    return score, reasons


def build_candidates(title: str, body: str, limit: int = 14) -> list[dict]:
    lead = (body or "")[:600]
    title_words = content_words(title)
    body_words = content_words(body or "")

    freq = Counter(w for w, _ in title_words + body_words)
    title_set = {w for w, _ in title_words}
    lead_set = {w for w, _ in content_words(lead)}
    pos_of = {w: p for w, p in title_words + body_words}

    pool: dict[str, tuple[str, bool, bool]] = {}
    for w, p in title_words + body_words:
        pool.setdefault(w, (p, w in title_set, w in lead_set))

    # adjacent content-word compounds, e.g. 男性 + 困境 -> 男性困境
    for source in (title_words, body_words):
        for (w1, p1), (w2, p2) in zip(source, source[1:]):
            combo = w1 + w2
            if not (3 <= len(combo) <= 4):
                continue
            if w1 in STOPWORDS or w2 in STOPWORDS:
                continue
            if p1 in BAD_POS or p2 in BAD_POS:
                continue
            if combo in pool:
                continue
            pool[combo] = ("n", combo in title, combo in lead)
            if combo in title:
                title_set.add(combo)

    # noun compounds split by a light particle, e.g. 当代男性的五大困境
    # -> 男性 + 困境 = 男性困境. Only nouns, only a short gap, and the gap may
    # contain nothing but particles / counters.
    GAP_OK = re.compile(r"^[的之等个种些大\d一二三四五六七八九十两]*$")
    NOUN_POS = {"n", "nr", "ns", "nt", "nz", "ng", "vn", "an"}
    for source, in ((title_words,),):
        tagged = tag(source if isinstance(source, str) else title)
        # walk the raw token stream so we can measure the gap between nouns
        toks = [(w, p) for w, p in tagged]
        for i in range(len(toks)):
            for j in range(i + 1, min(i + 4, len(toks))):
                w1, p1 = toks[i]
                w2, p2 = toks[j]
                if p1 not in NOUN_POS or p2 not in NOUN_POS:
                    continue
                gap = "".join(w for w, _ in toks[i + 1 : j])
                if not GAP_OK.match(gap):
                    continue
                combo = w1 + w2
                if not (3 <= len(combo) <= 4) or combo in pool:
                    continue
                pool[combo] = ("n", combo in title, combo in lead)
                if combo in title:
                    title_set.add(combo)

    scored = []
    for word, (pos, in_title, in_lead) in pool.items():
        s, reasons = score_candidate(word, pos, in_title, in_lead, freq.get(word, 1))
        if s < 3.0:
            continue
        scored.append({
            "text": word,
            "chars": len(word),
            "pos": pos,
            "score": round(s, 1),
            "in_title": in_title,
            "freq": freq.get(word, 1),
            "reasons": reasons,
        })

    scored.sort(key=lambda c: (-c["score"], -c["chars"]))
    kept: list[dict] = []
    for cand in scored:
        # Only drop a candidate that is a fragment of a *much* better longer one.
        # A 2-char concept is a legitimate headline in its own right ("内耗",
        # "希望") and must not be discarded just because it sits inside a
        # 4-char compound ("内耗指南").
        if any(
            cand["text"] in k["text"]
            and cand["text"] != k["text"]
            and len(cand["text"]) < 3
            and k["score"] >= cand["score"] + 4.0
            for k in kept
        ):
            continue
        kept.append(cand)
        if len(kept) >= limit:
            break
    return kept


def build_subtitles(title: str, body: str, headline: str, limit: int = 6) -> list[str]:
    """4-8 character phrases for the small lower tier.

    The subtitle exists to add back the precision the big headline throws away,
    so prefer phrases that carry a tension or promise word over arbitrary body
    fragments.
    """
    core = EPISODE_PREFIX_RE.sub("", title).strip()
    for _ in range(3):
        core = TITLE_TAIL_RE.sub("", core).strip()
    core = re.sub(f"[^{CJK}0-9]+", "", core)
    if headline and headline in core:
        core = core.replace(headline, "", 1)

    pool: list[tuple[float, str]] = []

    def consider(phrase: str, base: float):
        phrase = re.sub(r"\d+", "", phrase)  # stray episode numbers read badly
        phrase = re.sub(f"[^{CJK}]+", "", phrase)
        if not (4 <= len(phrase) <= 8) or phrase == headline or phrase in STOPWORDS:
            return
        if LIST_RE.search(phrase):
            return
        # a phrase ending on a particle/adverb is a truncated fragment
        if phrase[-1] in "的 是 越 就 而 在 把 被 让 和 与 及 或 也 都 很 更 最 不 没":
            return
        score = base
        if morpheme_hits(phrase, TENSION):
            score += 3.0
        if morpheme_hits(phrase, PROMISE):
            score += 2.6
        if len(phrase) in (4, 5, 6):
            score += 1.0
        pool.append((score, phrase))

    consider(core, 5.0)

    for line in (body or "").splitlines():
        line = line.strip()
        if len(line) < 12:
            continue
        for clause in re.split(r"[，。！？；：,.!?;]", line):
            consider(clause, 2.5)

    for w, _ in content_words(title):
        consider(w, 2.0)

    pool.sort(key=lambda t: -t[0])
    seen, result = set(), []
    for _, phrase in pool:
        # skip near-duplicates: "第一种内耗" vs "第二种内耗" is one idea, not three
        chars = set(phrase)
        if any(len(chars & set(k)) / max(1, len(chars | set(k))) > 0.6 for k in result):
            continue
        if phrase not in seen:
            seen.add(phrase)
            result.append(phrase)
        if len(result) >= limit:
            break
    return result


# --------------------------------------------------------------------------- #
# cli
# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--title", help="article title")
    ap.add_argument("--body", help="path to the article body (txt/md/html)")
    ap.add_argument("--url", help="fetch the article from a URL (e.g. a WeChat article)")
    ap.add_argument("--top-label", help="the small label above the headline, e.g. '第 26 集'")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of a report")
    ap.add_argument("--limit", type=int, default=14)
    ap.add_argument("--keep-traditional", action="store_true",
                    help="skip the Traditional->Simplified conversion")
    args = ap.parse_args()

    if not _JIEBA:
        print("[text] WARNING: jieba not installed - falling back to crude CJK runs, "
              "results will be much worse", file=sys.stderr)

    body = ""
    if args.body:
        p = Path(args.body)
        if not p.exists():
            raise SystemExit(f"error: body file not found: {args.body}")
        raw = p.read_text(encoding="utf-8", errors="ignore")
        body = strip_html(raw) if p.suffix.lower() in (".html", ".htm") else raw
    if args.url:
        print(f"[text] fetching {args.url}", file=sys.stderr)
        body = fetch_article(args.url)

    title = args.title
    if not title:
        if not body:
            raise SystemExit("error: pass --title, or --body/--url containing a title")
        title = next((ln.strip() for ln in body.splitlines() if len(ln.strip()) > 4), "")

    original_title = title
    if not args.keep_traditional:
        title = to_simplified(title)
        body = to_simplified(body)

    if not CJK_RE.search(title):
        raise SystemExit("error: this designer is for Chinese titles")

    candidates = build_candidates(title, body, args.limit)
    if not candidates:
        raise SystemExit("error: no viable candidates - is the text long enough?")

    headline = candidates[0]["text"]
    subtitles = build_subtitles(title, body, headline)

    if args.json:
        print(json.dumps(
            {"title": title, "original_title": original_title,
             "headline_candidates": candidates,
             "subtitle_candidates": subtitles, "top_label": args.top_label},
            ensure_ascii=False, indent=2))
        return

    if title != original_title:
        print(f"原标题：{original_title}")
        print(f"转简体：{title}")
    else:
        print(f"原文标题：{title}")
    if body:
        print(f"正文字数：{len(CJK_RE.findall(body))} 字")
    print()
    print("=" * 76)
    print("大字候选（2–4 字，按推荐度排序）")
    print("=" * 76)
    print(f"{'排名':<5}{'文字':<9}{'字数':<6}{'词性':<6}{'得分':<7}{'标题':<5}理由")
    print("-" * 76)
    for i, c in enumerate(candidates, 1):
        print(
            f"{i:<5}{c['text']:<9}{c['chars']:<6}{c['pos']:<6}{c['score']:<7}"
            f"{'★' if c['in_title'] else ' ':<5}{'、'.join(c['reasons'])}"
        )
    print()
    print("=" * 76)
    print("副标题候选（4–8 字，放小字层）")
    print("=" * 76)
    for s in subtitles or ["（未提取到，建议自己写一句）"]:
        print(f"  · {s}")
    print()
    print("=" * 76)
    print("选用建议")
    print("=" * 76)
    top3 = " / ".join(c["text"] for c in candidates[:3])
    print(f"  大字：从 {top3} 里选。优先选含「冲突/情绪」或「具象」字的那个。")
    print(f"  上方小字：{args.top_label or '栏目名或期数，如「第 26 集」'}")
    print(f"  下方小字：{subtitles[0] if subtitles else '自拟一句 4–8 字'}")
    print()
    print("  ⚠️ 列表标记词（三个/六种/五点）已重罚，不适合做封面大字。")
    print("  ⚠️ 这是候选生成器不是裁判。读一遍，凭语感定稿。")


if __name__ == "__main__":
    main()
