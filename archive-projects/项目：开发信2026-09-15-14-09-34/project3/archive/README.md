# archive · 已弃用资产与历史存档

> **本目录只读参考，正常写作流程不需要看。**
> 存档于 2026-09-23（分层改造）。

---

## 一、已弃用的签名图片方案

**弃用原因**：用户用**企业微信邮箱**发送，**无服务器权限、无法上传图片到公网** →
图片必然破图。**已决定：邮件签名一律用纯文字。**

| 文件 | 原用途 |
|---|---|
| `email-signature-embedded.html` | 图片 base64 内嵌版（曾试图绕过破图）|
| `email-signature-photo.html` | 带头像图片的签名版 |
| `email-signature.html` | 早期签名 HTML 版 |
| `signature-card.png` / `signature-card.jpg` | 整张名片做成的图片 |
| `assets/`（banner.png / pic.jpg / pic-156.jpg）| 签名用图 |

**✅ 替代品（仍在使用）**：
- `email-signature-text.html` —— 三套**纯文字**方案（主交付）
- `email-signature-plain.txt` —— 纯文本版（给会剥 HTML 的 CRM）
- `邮箱名片-说明.md` —— 签名最终版说明

---

## 二、历史文档

| 文件 | 说明 |
|---|---|
| `图片显示问题-解决方案.md` | 记录"图片为什么破图"及两种解法。**结论已被 `邮箱名片-说明.md` 吸收**，此处仅作过程留档 |

---

## 三、⚠️ 已停用的外部文件（不在本目录，仅登记）

### `C:\Users\win\Desktop\cold-email-portable.md`（145 行）— **已停用**

- **停用日期**：2026-09-23（分层改造时）
- **原因**：其全部内容已并入 `project3/01_skill_email_writing.md`

| portable 的内容 | 已并入 |
|---|---|
| A/B/C 三骨架 | `01_skill_email_writing.md` §二 |
| 输出格式 | §一 |
| 自检表 | §二自检 + `04_do_not_say.md` §九 |
| 毅冰核心纪律 | §二「核心纪律」 |
| 我方公司信息 YAML | 原是"待填"占位 → 实际内容在 `02_product_positioning.md` + `jzp-company-knowledge` 技能 |

> 🔴 **今后只维护 `project3/01_skill_email_writing.md`，不要再改 portable。**
> 原件**停留原地不动**（用户决定），仅作历史留存。

---

## 四、⚠️ 跟进表口径（重要）

### `C:\Users\win\Desktop\ian开发信跟进表.et` — **用户自用副本，不作数据源**

| | 本项目（✅ 标准）| Desktop 副本 |
|---|---|---|
| 文件 | `开发信跟进表.xlsx` | `ian开发信跟进表.et` |
| 修改时间 | **2026-09-23** | 2026-09-18（**已过期 5 天**）|
| 格式 | xlsx（下拉/配色/冻结/筛选）| WPS `.et` |

> 🔴 **唯一标准 = 本项目 `开发信跟进表.xlsx`**（+ 文本备份 `开发信跟进表.md`）。
> **不要反向同步** —— Desktop 副本已过期，合并会污染数据。
> 需要桌面副本时，**从本项目 xlsx 导出覆盖**。
> Desktop 的 `.et` 属用户个人文件，**本工具不移动、不删除、不修改**。

---

## 五、不属于本项目的资产

| 文件/目录 | 说明 |
|---|---|
| `opencode-toolchain/.opencode/` | opencode（另一款 AI 工具）的工具链残留（含 node_modules）。非 WorkBuddy 资产，未被本项目任何文件引用 → 整体归档 |
| ~~`移交项目2-canada-b2b-prospecting-SKILL.md`~~ | **已移至** `project3/待移交-项目2-canada-b2b-prospecting/`（自包含结构，待用户移交到「找客户」项目）|

---

## 六、如需恢复

所有文件在分层改造前均已整体备份：
`C:\Users\win\WorkBuddy AI\BACKUP-开发信项目-20260923-1408\`

