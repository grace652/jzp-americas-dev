#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 batch11 目标客户清单 CSV（50 家）。编号 424–473。"""
import csv
from pathlib import Path

BASE = Path("/Users/eric/WorkBuddy AI/2026-09-27-00-43-30/jzp-americas-dev/线索资产")

# (编号, 类型, 公司全称, 简称, 国家, 州省, 城市, 官网, 业务描述原句, 高价值档, 来源, 核实状态)
ROWS = [
    # ── A 类 · 加拿大（424–438）──
    (424, "A 电气承包商/工程公司", "F&M Installations Ltd.", "FMI", "加拿大", "BC", "Mission", "fminstallations.ca",
     "a top Western Canadian contractor with 30+ years' experience, specializes in utility electrical infrastructure, delivering 200+ substations", "⭐", "ECABC 会员名录（BC 省电气承包商协会）", "✅ 入选"),
    (425, "A 电气承包商/工程公司", "Chemco Electrical Contractors Ltd.", "Chemco", "加拿大", "AB", "Nisku", "chemco.com",
     "we're more than contractors—we're industry builders with over 60 years of excellence. As an employee-owned Canadian company", "⭐", "ECAA 会员名录（AB 省电气承包商协会）", "✅ 入选"),
    (426, "A 电气承包商/工程公司", "Tripower Electrical Services Ltd.", "Tripower", "加拿大", "BC", "Nanaimo", "tripowerhv.com",
     "Specializing in MV and HV cabling… testing for all Medium Voltage (1kV-100kV) and High-Voltage (100kV+)", "⭐", "ECABC 会员名录", "✅ 入选"),
    (427, "A 电气承包商/工程公司", "Accurate Power Group Ltd.", "Accurate Power", "加拿大", "BC", "Vancouver", "accuratepowergroup.com",
     "Red Seal power system Electricians and Certified Infrared Thermographers provide… commissioning, maintenance, testing, repairs, upgrades and installations of electrical power distribution systems", "⭐", "ECABC 会员名录", "✅ 入选"),
    (428, "A 电气承包商/工程公司", "AVC Industrial Inc.", "AVC Industrial", "加拿大", "BC", "Surrey", "avcwest.com",
     "Design Builds, Maintenance & Service, High Voltage or any other service you might require for your projects and plants. FSR-A High Voltage Work Available", "⭐", "ECABC 会员名录", "✅ 入选"),
    (429, "A 电气承包商/工程公司", "Harrison Industrial Contracting Ltd.", "Harrison Industrial", "加拿大", "BC", "Kamloops", "harrisonindustrial.ca",
     "We provide complete industrial electrical support… the unique skills to maintain pumping systems, substations, building infrastructure, traffic & controls, lighting", "⭐", "ECABC 会员名录", "✅ 入选"),
    (430, "A 电气承包商/工程公司", "WSG Energy Services", "WSG Energy", "加拿大", "AB", "Leduc", "wsgenergyservices.com",
     "Turnkey HV Installations / Turnkey Electrical & Instrumentation Installations", "⭐", "ECAA 会员名录", "✅ 入选"),
    (431, "A 电气承包商/工程公司", "Crew Electrical Ltd.", "Crew Electrical", "加拿大", "AB", "Edmonton", "crewelectrical.ca",
     "As a locally owned and operated Electrical Contractor in the Edmonton and greater area… Industrial: Modular Projects, Controls, Commissioning and Decommissioning", "—", "ECAA 会员名录", "✅ 入选"),
    (432, "A 电气承包商/工程公司", "Raylec Power LP", "Raylec Power", "加拿大", "BC", "Courtenay", "raylecpower.ca",
     "a versatile electrical maintenance contracting company specializing in electrical construction, complex electrical system installations", "—", "ECABC 会员名录", "✅ 入选"),
    (433, "A 电气承包商/工程公司", "Custom Electric Ltd.", "Custom Electric", "加拿大", "AB", "Calgary", "customelectric.com",
     "one of southern Alberta's largest independent electrical contractors… workforce of approximately 375 tradespeople and office staff", "—", "ECAA 会员名录", "✅ 入选"),
    (434, "A 电气承包商/工程公司", "Werner Electric Ltd.", "Werner Electric", "加拿大", "BC", "Surrey", "wernerelectric.ca",
     "we've proudly served Greater Vancouver… supporting large-scale industrial facilities", "—", "ECABC 会员名录", "✅ 入选"),
    (435, "A 电气承包商/工程公司", "Wescan Construction Services", "Wescan", "加拿大", "MB", "Winnipeg", "wescan-services.com",
     "began operations as Wescan Electric in 1978 to provide design and contract services in the electrical field… proud to be an Indigenous-owned business", "—", "ECAM 会员名录（MB）", "✅ 入选"),
    (436, "A 电气承包商/工程公司", "Mazzei Electric Ltd.", "Mazzei Electric", "加拿大", "BC", "Nanaimo", "mazzeielectric.com",
     "Providing a Range of Industrial, Commercial and Residential Electrical Services across British Columbia. With over 300 electricians", "—", "ECABC 会员名录", "✅ 入选"),
    (437, "A 电气承包商/工程公司", "Cdn. Power PAC", "CDN Power PAC", "加拿大", "AB", "Acheson", "cdnpowerpac.com",
     "among the largest Institutional & Commercial Electrical & Solar Contractors in the Province of Alberta specializing in Educational, Healthcare, Light-Industrial, Transit, Recreational", "—", "ECAA 会员名录", "✅ 入选"),
    (438, "A 电气承包商/工程公司", "Tri-Star Electric Company Ltd.", "Tri-Star Electric", "加拿大", "MB", "Winnipeg", "tristar.ca",
     "provides expert electrical installation and maintenance for a variety of industrial, commercial, multiple residential and government clients", "—", "ECAM 会员名录", "✅ 入选"),

    # ── A 类 · 美国（439–448）──
    (439, "A 电气承包商/工程公司", "VEC, Inc.", "VEC", "美国", "OH", "Girard", "vecohio.com",
     "Our constructors produce the infrastructure to handle high-voltage substation construction as well as self-sufficient microgrids", "⭐", "NECA North Central Ohio 会员名录", "✅ 入选"),
    (440, "A 电气承包商/工程公司", "Agostino Utilities LLC", "Agostino", "美国", "PA", "Schwenksville", "agostinoutilities.com",
     "substation + high voltage + transmission（官网服务栏）", "⭐", "NECA Penn-Del-Jersey 承包商名录", "✅ 入选"),
    (441, "A 电气承包商/工程公司", "Battaglia Electric, Inc.", "Battaglia", "美国", "PA", "Tinicum Township", "battag.com",
     "transmission + substation（官网服务栏）", "⭐", "NECA Penn-Del-Jersey 承包商名录", "✅ 入选"),
    (442, "A 电气承包商/工程公司", "H.B. Frazer Company", "H.B. Frazer", "美国", "PA", "Phoenixville", "hbfrazer.com",
     "utility line + high voltage（官网服务栏）", "⭐", "NECA Penn-Del-Jersey 承包商名录", "✅ 入选"),
    (443, "A 电气承包商/工程公司", "Albarell Electric, Inc.", "Albarell", "美国", "PA", "Bethlehem", "albarell.com",
     "high voltage（官网服务栏）", "⭐", "NECA Penn-Del-Jersey 承包商名录", "✅ 入选"),
    (444, "A 电气承包商/工程公司", "Enerfab Power & Industrial", "Enerfab", "美国", "OH", "Cincinnati", "enerfab.com",
     "电力/重工业施工与维护（Power & Industrial 事业部）", "—", "NECA North Central Ohio 会员名录", "✅ 入选"),
    (445, "A 电气承包商/工程公司", "White Electrical Construction Company", "White Electrical", "美国", "GA", "Columbus", "white-electrical.com",
     "大型工业电气承包商，1910 年创立于 Rome, GA", "—", "AECA（Atlanta 分会）会员名录", "✅ 入选"),
    (446, "A 电气承包商/工程公司", "Inglett & Stubbs, LLC", "Inglett & Stubbs", "美国", "GA", "Mableton", "inglett-stubbs.com",
     "综合电气施工（Atlanta 都会区）", "—", "AECA（Atlanta 分会）会员名录", "✅ 入选"),
    (447, "A 电气承包商/工程公司", "C3M Power Systems LLC", "C3M Power", "美国", "MD", "Capitol Heights", "c3mpowersystems.com",
     "交通/基础设施电力施工", "—", "NECA Washington DC 会员名录", "✅ 入选"),
    (448, "A 电气承包商/工程公司", "Hatzel & Buehler, Inc.", "Hatzel & Buehler", "美国", "PA", "Philadelphia", "hatzelandbuehler.com",
     "Established in 1884… the oldest Electrical Contractor in the United States", "—", "NECA Penn-Del-Jersey 承包商名录", "✅ 入选"),

    # ── B 类 · 加拿大（449–458）──
    (449, "B 分销商/贸易商", "Moncur Electric Supply Ltd.", "Moncur", "加拿大", "ON", "Windsor", "moncurelectric.com",
     "As a premier electrical supplier, Moncur Electric Supply prides itself on offering a comprehensive range of high-quality products… Lighting, distribution, conduit, fittings, cable, data, fuses, enclosures, transformers", "⭐", "定向检索（Windsor ON electrical supply）", "✅ 入选"),
    (450, "B 分销商/贸易商", "Electrical Material Company (E.M.C. Ltd.)", "E.M.C.", "加拿大", "ON", "Hamilton", "electricalmaterials.ca",
     "a great source for new, used, and surplus electrical materials… As authorized distributors… Rex transformers, Marcus transformers, Bemag transformers", "⭐", "定向检索（Hamilton ON surplus dealer）", "✅ 入选"),
    (451, "B 分销商/贸易商", "Parrline Supply", "Parrline", "加拿大", "ON", "Windsor", "parrline.com",
     "a proud, family run, third generation independent business in Windsor Essex County… a mainstay in the electrical distribution industry", "—", "定向检索", "✅ 入选"),
    (452, "B 分销商/贸易商", "Northern Breaker Group", "NBG", "加拿大", "AB", "Calgary", "northernbreakergroup.ca",
     "Western Canada's premier electrical supply network… New, Used & Obsolete Products…（品类页含 REX 变压器）", "⭐", "Surplus Record 断路器经销商目录", "✅ 入选"),
    (453, "B 分销商/贸易商", "Carroll Transformer & Switchgear", "Carroll", "加拿大", "ON", "Tillsonburg", "carrolltransformer.ca",
     "a 'dedicated' high voltage substation distribution company, providing engineered-product solutions for the North American marketplace… our network of global supply partners", "⭐", "Surplus Record 变压器经销商目录", "✅ 入选"),
    (454, "B 分销商/贸易商", "EcoTech NL Inc.", "EcoTech", "加拿大", "NL", "St. John's", "ecotechnl.ca",
     "specializes in new and repurposing of electrical equipment such as switchgear, motor control centers, panel boards, e-houses, and transformers", "⭐", "定向检索（Newfoundland electrical supply）", "⚠️ 条件入选（见风险）"),
    (455, "B 分销商/贸易商", "Powerlogy", "Powerlogy", "加拿大", "ON", "Mississauga", "powerlogy.ca",
     "both an electrical supply wholesale destination and a full-service electrical store… Bulk offerings for contractors, including panelboards, switchgear", "⭐", "定向检索", "✅ 入选"),
    (456, "B 分销商/贸易商", "O'Neil Electric Supply Ltd.", "O'Neil", "加拿大", "ON", "Woodbridge", "oneilelectric.com",
     "Independent Wholesale Supplier of Premium Electrical Products in Ontario and the GTA for over 50 years", "—", "定向检索", "✅ 入选"),
    (457, "B 分销商/贸易商", "Argo International Corp", "Argo", "加拿大", "ON", "Burlington", "argointl.com",
     "has been in business since 1952… Transformers — Dry type, Machine Tool, Pad Mount, Oil filled, Auto transformer, and Control transformers", "⭐", "CTI 名录（Control & Distribution Transformers Suppliers, ON）", "✅ 入选"),
    (458, "B 分销商/贸易商", "Lakeport Power Ltd.", "Lakeport", "加拿大", "ON", "Colborne", "lakeportpower.com",
     "an electrical utility supply distributor, servicing utilities and their contractors… we supply brand new transformers from industry-leading manufacturers, fabricated to your exact specifications", "⭐", "Surplus Record 变压器经销商目录", "✅ 入选（⭐ 最高优先）"),

    # ── B 类 · 美国（459–473）──
    (459, "B 分销商/贸易商", "CTG Power Systems International", "CTG Power", "美国", "FL", "Tampa", "ctgpowersystems.com",
     "a global supplier of new and reconditioned power generation and high voltage electrical equipment… We take title and stand behind the equipment. Not a broker", "⭐", "官网直查（二手电力设备垂直平台）", "✅ 入选（⭐ 最高优先）"),
    (460, "B 分销商/贸易商", "Piela Electric, Inc.", "Piela Electric", "美国", "CT", "Preston", "pielaelectric.com",
     "Since 1932… electrical and mechanical power transmission equipment… with our extensive inventory of new and surplus equipment. Fuses, transformers, circuit breakers… is our forte", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (461, "B 分销商/贸易商", "Cowtown Breakers LLC", "Cowtown Breakers", "美国", "TX", "Fort Worth", "cowtownbreakers.com",
     "over 50 years of experience in the electrical distribution industry… Buy, Sell or Recover Industrial And Commercial Electrical Power Distribution Equipment（含 Substation / Pad Mount / Dry Type Transformers）", "⭐", "官网直查", "✅ 入选"),
    (462, "B 分销商/贸易商", "Breakers & Beyond LLC", "Breakers & Beyond", "美国", "GA", "Cumming", "breakersbeyond.com",
     "buying, and removing electrical equipment across Georgia, South Carolina, North Carolina, Tennessee, Alabama… from circuit breakers and switchgear to transformers（dry-type and oil-filled）", "⭐", "官网直查", "✅ 入选"),
    (463, "B 分销商/贸易商", "Electrical Service Products, Inc.", "ESP", "美国", "WA", "Spokane", "espelectrical.com",
     "stocks a full-range of new and reconditioned switchgear, circuit breakers, motor control parts, power fuses, dry-type transformers, relays, distribution equipment", "⭐", "官网直查", "✅ 入选"),
    (464, "B 分销商/贸易商", "Romanoff Industries, Inc.", "Romanoff", "美国", "OH", "Toledo", "romanoffindustries.com",
     "Buys and sells used, reconditioned, and new surplus electric motors, transformers and circuit breakers", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (465, "B 分销商/贸易商", "Current Midwest, LLC", "Current Midwest", "美国", "IN", "Michigan City", "currentmidwest.com",
     "large inventory of dry type transformers for industrial installations, including single and three phase units ranging from 1 to 2500 kVa. We offer new Federal Pacific and Rex Power Magnetics products", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (466, "B 分销商/贸易商", "Midwest Machinery Mart", "Midwest Machinery Mart", "美国", "IN", "Indianapolis", "mid-westmachinerymart.com",
     "We specialize in new and used industrial electrical equipment. We stock all kinds of motors, motor starters, circuit breakers, transformers, frequency drives", "⭐", "官网直查", "✅ 入选"),
    (467, "B 分销商/贸易商", "Integrity Electric Direct", "Integrity Electric", "美国", "IN", "Indianapolis", "integrityelectricdirect.com",
     "Some of the items we carry include breakers, disconnects, switch gears, transformers, bus plugs, bus ducts, programmable instruments, generators", "⭐", "官网直查", "✅ 入选"),
    (468, "B 分销商/贸易商", "Woodstock Power Co.", "Woodstock Power", "美国", "PA", "Philadelphia", "woodstockpower.com",
     "We deal with quality and affordable electrical systems ranging from: generators, switchgear, breakers, transformers, and more", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (469, "B 分销商/贸易商", "Powerhouse Systems LLC", "Powerhouse Systems", "美国", "TN", "Niota", "powerhouse-systems.com",
     "We specialize in decommissioning entire data centers and industrial facilities — buying the electrical equipment, coordinating removal, and reselling it… generators, circuit breakers, switchgear, UPS systems, and transformers", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (470, "B 分销商/贸易商", "Sully Enterprises Inc.", "Sully Enterprises", "美国", "UT", "West Jordan", "sullyent.com",
     "Looking for spare substation or generation class transformers? We buy, sell, and scrap your surplus new & used power transformers", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (471, "B 分销商/贸易商", "Megawatt Equipment Co.", "Megawatt", "美国", "TX", "Fulshear", "megawattequipment.com",
     "America's #1 Buyer of Substation Transformers & Electrical Equipment… purchasing large power transformers, pad-mounted transformers, SF6 breakers, switchgear", "⭐", "Surplus Record 经销商目录", "✅ 入选"),
    (472, "B 分销商/贸易商", "Safe Power Distributors, Inc.", "Safe Power", "美国", "FL", "Palm Harbor", "safepowerusa.com",
     "specializes in purchasing used transformers — including dry-type, pad-mount, liquid-filled, and substation units", "⭐", "Surplus Record 经销商目录", "⚠️ 条件入选（MX 走 Proofpoint）"),
    (473, "B 分销商/贸易商", "Bruce Electric Equipment Corp.", "Bruce Electric", "美国", "NY", "Lindenhurst", "brucelectric.com",
     "one of the largest electrical equipment supplier and master stocking distributors of quality Electrical Distribution Equipment including Dry Type Transformers, Switchgear", "⭐", "Surplus Record 经销商目录", "⚠️ 条件入选（干式专营，产品错配）"),
]

HEAD = ["序号", "类型", "公司全称", "简称", "国家", "州省", "城市", "官网",
        "业务描述原句", "高价值档", "来源", "核实状态"]

out = BASE / "目标客户清单-batch11.csv"
with out.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(HEAD)
    for r in ROWS:
        w.writerow(r)

# 统计
from collections import Counter
print(f"写出 {len(ROWS)} 行 -> {out.name}")
print("类型：", Counter(r[1] for r in ROWS))
print("国家：", Counter(r[4] for r in ROWS))
print("高价值档：", Counter(r[9] for r in ROWS))
print("州省分布：", Counter(f"{r[4][:2]}{r[5]}" for r in ROWS))
print("编号范围：", ROWS[0][0], "-", ROWS[-1][0])
