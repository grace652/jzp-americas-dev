---
name: wechat-article-harvest
description: 抓取微信公众号文章正文与账号文章列表（限速、不绕验证码）。当用户说「抓公众号文章」「下载公众号正文」「公众号对标」「看看某公众号发了什么」「爬微信公众号」或需要批量获取 mp.weixin.qq.com 文章时使用。覆盖搜狗搜索发现账号、解析跳转拿到真实 URL、合集(专辑)接口免登录枚举文章、正文提取的完整机制与反爬应对。
agent_created: true
---

# 微信公众号文章抓取

**核心结论先说**：正文页 `mp.weixin.qq.com/s/...` **无验证墙、无需登录**，直接 curl 就能抓。
难点只在**怎么拿到文章 URL**——下面两条机制已实测打通。

## 一、抓正文（最简单，优先用这条）

```bash
curl -sL --max-time 45 \
  -A "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1" \
  "https://mp.weixin.qq.com/s/XXXX" -o page.html
```

从 HTML 提取（正则即可，不必装 bs4）：
- 正文：`id="js_content"`，按 **div 深度匹配**截取（`<div` / `</div>` 计数归零）
- 标题：`<h1 id="activity-name">` 或 `var msg_title`
- 账号名：`var nickname = htmlDecode("...")`
- **微信号**：`var user_name = "gh_xxxxxxxx"`
- `__biz`：`var biz = "..."`
- 发布时间：`var ct = "<时间戳>"`

正文 HTML → 文本时把 `<img>` 换 `[图片位置]`、`<br>` 换换行、块级标签换双换行。
参考实现：`~/Documents/写作风格特征拆解/写作风格特征拆解/样本/微信公众号-请知/fetch_raw_format.py`（曾 24/24 成功）。

## 二、拿 URL 的机制 A：搜狗按「微信号」或「账号名」搜索

```bash
# 按账号名搜索（结果应全部归属该账号）
https://weixin.sogou.com/weixin?type=2&query=冯站长之家
# 按微信号搜索 —— ⚠️ 效果不稳定，先试再依赖
https://weixin.sogou.com/weixin?type=2&query=gh_07ce994491d9
```

**按微信号搜索的实测结果（别盲目依赖）**：
- 「有些信号」`gh_07ce994491d9` → 4 篇全归属 ✓ 有效
- 「武志红」`gh_f99a5327b51a` → 10 条，但**全来自别的账号**（特鹅宝藏库等，
  只是文章里提到了这个微信号）✗ 无效
- 「刘润」`gh_cc764ea0efaa` → 0 条 ✗ 无效

结论：**微信号搜索不比账号名搜索更可靠**，小号可能有效，大号基本无效。两种都试，取归属正确的那条。

结果解析（结果块为 `<div class="txt-box">`）：
- 标题：`<h3><a href="/link?url=...">标题</a>`
- **来源账号**：`<span class="all-time-y2">账号名</span>`
- 时间：`timeConvert('<时间戳>')`
- 摘要：`<p class="txt-info">`

⚠️ **`type=1`（账号搜索）已死**，任何词都返回"暂无…官方认证订阅号"。只能用 `type=2`。

## 三、拿 URL 的机制 B：解析搜狗 `/link?url=` 跳转 ★关键

直接请求 `/link?url=...` 会 302 到 `/antispider/`。**正确姿势**：

```bash
# 1) 先请求搜索页，把 cookie 写进 jar
curl -s -c jar.txt -b jar.txt -A "$DESKTOP_UA" "https://weixin.sogou.com/weixin?type=2&query=..." -o search.html
# 2) 带同一个 jar + Referer 请求 /link
curl -s -c jar.txt -b jar.txt -A "$DESKTOP_UA" -e "https://weixin.sogou.com/" \
     "https://weixin.sogou.com/link?url=..." -o link.html
```

`link.html` 里真实 URL 被**拆成多段**：

```js
var url = '';
url += 'https://mp.';
url += 'weixin.qq.c';
url += 'om/s?src=11';
...
window.location.replace(url)
```

**把所有 `url += '...'` 拼接起来**即得
`https://mp.weixin.qq.com/s?src=11&timestamp=...&signature=...`

⚠️ **签名 URL 有时效**（含 timestamp），**解析后必须立即抓正文**，不能存起来以后用。

## 三·补 拿 URL 的机制 C：合集（专辑）接口 ★免登录可用，优先级最高

**2026-10-01 实测新增**：只要拿到**任意一篇**该账号文章，就能从正文页源码里挖出
`album_id`，再用**免登录**的合集接口把该合集下的文章**全量**拉出来（含标题、时间、mid、sn）。

```bash
# 1) 从文章页提取（正则即可）
#    var biz = "..."            -> __biz
#    user_name: 'gh_xxxx'       -> 微信号
#    album_id: '4654812332404080643'
# 2) 调合集接口
curl -sL --max-time 45 -A "$MOBILE_UA" -e "https://mp.weixin.qq.com/" \
  "https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&__biz=<biz>&album_id=<album_id>&count=100&f=json"
```

返回 `{"base_resp":{"ret":0},"getalbum_resp":{...}}`，关键字段：
- `article_list[]` —— 每项含 `title` / `create_time`（秒级时间戳）/ `msgid` / `itemidx` / `url`
- `base_info.article_count` —— 合集总篇数
- `continue_flag` —— `0` 表示无下一页
- `base_info.public_tag_content_num` —— **话题标签**下的内容数，**不等于**账号文章数（话题允许他号投稿）

⚠️ **合集 ≠ 账号全量**。实测同一账号存在「msgid 落在合集区间内、却不在合集列表里」的文章
（说明合集是人工精选）。**不要把合集篇数当作账号总篇数**，除非另有证据。

同时实测**不可用**的相邻接口（全部 `ret:-3, errmsg:"no session"`）：
| 接口 | 结果 |
|---|---|
| `appmsgalbum?action=get_album_list`（列全部合集） | ❌ no session |
| `mp/publictag?action=get`（话题标签内容） | ❌ no session |
| `mp/appmsg_comment?action=getcomment`（留言） | ❌ no session |

**能拿到的账号标识**：文章页源码里 `var biz` / `user_name` / `var nickname`（账号名）齐全，
可用来跨渠道核验文章归属。

---

## 四、限速与反爬（必须遵守）

| 目标 | 间隔 |
|---|---|
| `weixin.sogou.com` | **15 秒/请求** |
| `mp.weixin.qq.com` | 3 秒/请求 |

- 限速做**持久化**（把上次请求时间写文件），否则连跑两次脚本会绕过间隔。
- 命中 `antispider` / `请依次点击` **立即中止**，记录后跳过。
  **不要解验证码**——那是绕过站点访问控制，且会加重 IP 封禁。
- 搜狗触发反爬的阈值很低：连续快速 curl 十几次就会被要求点汉字验证码，**按 IP 封**。

## 五、踩过的坑

- ❌ **浏览器自动化对搜狗无效**：真实 Chrome 也被拦（搜狗能识别自动化特征）。
  curl + 限速 反而更稳。
- ❌ **百度/必应 curl 也被拦**：百度跳 `wappass.baidu.com/.../captcha`；必应不返回文章 URL。
- ❌ **`profile_ext`（账号历史消息）** 免登录不可用 → "请在微信客户端打开链接"。
- ❌ **阅读量/在看数拿不到**：文章页 `appmsg_token` 是空字符串，`getappmsgext` 调不动。
  新榜/清博需付费。**不要估算，直接标"未获取"**。
  （2026-10-01 复核：`read_num`/`like_num`/`reward_total_count` 在正文页均为 `"" * 1` 空值；
  `mp/appmsg_comment` 留言接口返回 `no session`。**阅读、在看、留言三者公开渠道确认全部拿不到。**）
- ⚠️ **正文页批量请求必触发安全验证页**（2026-10-01 实测）：
  连续请求会返回 `mmbizwap:secitptpage/verify.html` + `captcha.gtimg.com/TCaptcha.js`。
  实测 3s / 15s / 25s / 50s 间隔**均被拦**；单次请求可成功。
  **冷却期比预期长**：静默 7 分钟后再请求**仍被拒**。不要用「退避几十秒重试」的思路，会白等。
  正确做法：**一次只抓 1–2 篇、失败即停、隔较长时间再续**，并做**断点续抓**（已抓到的落盘、下次跳过）。
- ⚠️ **Shell `curl` 与 Python `subprocess` 的 curl 出网路径可能不同**（2026-10-01 实测）：
  同一时刻、相同 UA、相同代理环境变量下，**Shell 直接 curl 拿到正文，Python subprocess 拿到验证页**。
  → 批量抓取**优先用 Shell curl 循环**，不要把 curl 塞进 Python `subprocess.run()`。
- ⚠️ **搜狗按账号名搜索可能完全失效**（2026-10-01 实测「有些信号」）：
  返回 10 条结果，归属账号**全部是别的账号**（只是文章里提到该号名），本账号 0 条。
  别看到有结果就以为可用，**必须逐条核对 `all-time-y2` 归属**。
- ❌ RSSHub `/wechat/mp/*` 路由已移除；wechat2rss.xlab.app 只覆盖安全/技术类账号。
- ⚠️ **后台任务不继承沙箱提权** → curl 写 cookie jar 会被拒。**必须前台跑**。
- ⚠️ **按账号名搜索会混入运营内容**（招聘帖、广告、星座运势），甚至命中"他人写该号主"的文章。
  分析前必须过滤：关键词命中 `招聘/招人/实习/校招/招募/运势/福利/优惠/抽奖` 的排除。

## 六、搜狗索引对成熟账号是陈旧的（重要预期管理）

实测：小号/新号收录及时（2026-09 的文章能搜到），**大号的索引停在 2016-2024**。
所以"按账号名搜索"**拿不到大号的近期文章**。
若必须要大号近期内容 → 让用户手动提供文章链接，或改用付费数据源。

## 七、完整脚本参考

`/Users/eric/Documents/有些信号对标分析/scripts/` 下有一套可直接复用的实现：
- `_common.py` —— 限速器、反爬检测、正文提取、账号台账
- `sogou_search.py` —— 搜狗搜索（发现 + 枚举）
- `fetch_via_sogou.py` —— **搜索 → 解析跳转 → 抓正文**（主力）
- `fetch_article.py` —— 已知 URL 直接抓正文
- `validate_candidates.py` —— 按账号名验证账号是否真实活跃（归属数）
- `digest.py` —— 生成"标题+开头+结尾"摘要，供分析
