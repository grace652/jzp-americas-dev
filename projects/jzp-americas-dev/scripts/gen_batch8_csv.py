#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 线索资产/目标客户清单-batch8.csv"""
import csv
from pathlib import Path

BASE = Path(Path(__file__).resolve().parents[1] / "线索资产")

HDR = ["序号", "类型", "公司全称", "简称", "国家", "州省", "城市", "官网",
       "业务描述原句", "高价值档", "来源", "核实状态"]

ROWS = [
    # ── A 类 · 加拿大 13 家（买家 274–286）────────────────────────────
    ["274", "A 电气承包商/工程公司", "Powerst (Power Substations and Transmission Co.)", "Powerst", "加拿大", "ON", "Pickering", "powerst.ca",
     "Powerst designs and builds the high voltage substations, transmission lines and renewable infrastructure that carry power from source to grid — delivered as PC, EPC and turnkey projects.", "⭐", "定向检索 HV substation EPC Canada", "✅ 入选"],
    ["275", "A 电气承包商/工程公司", "Powerline Plus Ltd.", "Powerline Plus", "加拿大", "ON", "Toronto (Scarborough)", "powerlineplus.com",
     "Our proven track record boasts successful project management and construction of high-voltage underground power vaults, substations, switching stations, gas-insulated switchgear (GIS), and interconnect stations ranging from 5kV to 44kV.", "⭐", "定向检索 substation contractor Canada", "✅ 入选"],
    ["276", "A 电气承包商/工程公司", "Site Plus Electrical Solutions Inc.", "Site Plus", "加拿大", "ON", "Brantford", "sitepluselectrical.ca",
     "Site Plus Electrical Solutions is one South Western Ontario's largest transformer installation service providers. We specialize in providing electric power transformers and related electrical equipment. We have experience with medium voltage to high voltage transformer installations.", "⭐", "定向检索 Ontario industrial electrical transformer installation", "✅ 入选"],
    ["277", "A 电气承包商/工程公司", "Gunson Power Corporation", "Gunson Power", "加拿大", "BC", "Aldergrove (Langley)", "gunsonpower.com",
     "We can build, maintain and repair wood structure transmission lines from 69 kv to 230 kV.", "⭐", "定向检索 BC powerline high voltage contractor", "✅ 入选"],
    ["278", "A 电气承包商/工程公司", "QED Technical Services Inc.", "QED Technical", "加拿大", "BC", "Kamloops", "qedts.com",
     "QED Technical Services specializes in the testing, commissioning, repair, and maintenance of electrical power system equipment. We have extensive experience working on heavy industrial sites, generating plants and high voltage substations.", "⭐", "定向检索 electrical contractor high voltage BC substation", "✅ 入选"],
    ["279", "A 电气承包商/工程公司", "JESCO Electrical Contractors Ltd.", "JESCO", "加拿大", "AB", "Airdrie", "jescoelectrical.ca",
     "JESCO has experience and expertise in the high voltage electrical components: General Inspections and Maintenance of High Voltage Equipment. We are COR certified and a member of ISNetworld.", "⭐", "定向检索 Alberta electrical contractor high voltage；ISNetworld", "✅ 入选"],
    ["280", "A 电气承包商/工程公司", "Ironclad Trades Co.", "Ironclad Trades", "加拿大", "AB", "Edmonton", "ironcladtrades.ca",
     "Ironclad Trades Co. provides specialized industrial electrical services led by Red Seal Industrial Electricians. We ensure high-voltage infrastructure and site power systems meet the technical rigor required for the Edmonton and Calgary industrial corridors.", "⭐", "定向检索 Alberta industrial electrical high voltage", "✅ 入选"],
    ["281", "A 电气承包商/工程公司", "DEI Électrique inc.", "DEI Électrique", "加拿大", "QC", "Saint-Mathieu-de-Beloeil", "deienergie.ca",
     "Entrepreneur electricien specialisé en electricite haute tension. Les travaux d'électricité haute tension dans les secteurs industriel et commercial exigent une grande rigueur.", "⭐", "CMEQ/RBQ 持牌承包商；定向检索 haute tension sous-station Québec", "✅ 入选"],
    ["282", "A 电气承包商/工程公司", "Pelletier et Picard inc.", "Pelletier et Picard", "加拿大", "QC", "Danville", "pelletierpicard.com",
     "PPI possède l'expertise et l'expérience nécessaires à vos travaux électriques de haute tension, en conception-construction et en automatisation, permettant d'offrir un véritable service clé en main sous un même toit.", "⭐", "CMEQ/RBQ 持牌承包商；定向检索", "✅ 入选"],
    ["283", "A 电气承包商/工程公司", "CIMA+ (CIMA Plus Société d'ingénierie)", "CIMA+", "加拿大", "QC", "Montréal", "cima.ca",
     "At CIMA+, we have over 40 years of proven experience in substation design and construction serving public utility companies, private developers, contractors, manufacturers, and industrial clients. Our experts have contributed to hundreds of projects involving the design of transmission, distribution and power generating substations from low-voltage to 735 kV.", "⭐", "定向检索 substation engineering Canada", "✅ 入选"],
    ["284", "A 电气承包商/工程公司", "PMP Powerline Construction Ltd.", "PMP Powerline", "加拿大", "SK", "Assiniboia", "pmppowerline.ca",
     "PMP Powerline offers maintenance and construction services for both overhead and underground power utilities. We have clients in several different lines of business including city power utilities, mining, oil well leases, rural, substations and Saskatchewan power utilities.", "⭐", "定向检索 Saskatchewan powerline substation；ISNetworld", "✅ 入选"],
    ["285", "A 电气承包商/工程公司", "Noble Electric Ltd.", "Noble Electric", "加拿大", "MB", "Winnipeg", "noble-electric.ca",
     "Noble Electric Ltd. is a licensed full-service Winnipeg electrical company serving businesses across Manitoba. We have extensive experience working with municipalities, mining operations and commercial contractors. Fully certified for high voltage, high-places.", "⭐", "定向检索 Manitoba high voltage contractor", "✅ 入选"],
    ["286", "A 电气承包商/工程公司", "S&H Power Services", "S&H Power", "加拿大", "NS", "Halifax", "sandhpowerservices.com",
     "Our high voltage industrial services include substations, street lighting, storm restoration and emergency response. Our team provides substation and powerline services to build, maintain and repair our electrical infrastructure and street lighting.", "⭐", "定向检索 Nova Scotia high voltage substation", "✅ 入选"],

    # ── A 类 · 美国 12 家（买家 287–298）─────────────────────────────
    ["287", "A 电气承包商/工程公司", "Saber Power Services, LLC", "Saber Power", "美国", "TX", "Houston", "saberpower.com",
     "Engineering-led & construction-focused professional services company specializing in complex medium & high voltage electrical infrastructure.", "⭐", "NETA 认证子公司；定向检索 substation high voltage electrical contractor Texas", "✅ 入选"],
    ["288", "A 电气承包商/工程公司", "Dashiell Corporation", "Dashiell", "美国", "TX", "Houston", "dashiell.com",
     "Dashiell is a leading national provider of high and medium voltage electrical services to the electric utility, power generation, industrial, and renewable energy industries. We provide a complete, turnkey service offering, including all engineering, procurement, construction, and testing and commissioning services.", "⭐", "定向检索 substation high voltage electrical contractor Texas", "✅ 入选"],
    ["289", "A 电气承包商/工程公司", "Diversified Substation Construction, LLC", "Diversified SCI", "美国", "FL", "Okeechobee", "diversifiedsci.com",
     "At Diversified Substation Construction, LLC., we specialize in comprehensive substation construction services. Our team manages all phases from design to commissioning, ensuring reliable electrical infrastructure. Leading experts in substation construction offering DSC services for projects from 23KV to 500KV.", "⭐", "定向检索 high voltage electrical contractor substation Florida design-build power", "✅ 入选"],
    ["290", "A 电气承包商/工程公司", "Highline Construction, Inc.", "Highline Construction", "美国", "MN", "Paynesville", "highlineconstructionmn.com",
     "Highline Construction is a premier power line company serving the Midwest since 1997 with distribution, transmission, substation, and more.", "⭐", "MMUA 供应商名录；定向检索 Minnesota substation", "✅ 入选"],
    ["291", "A 电气承包商/工程公司", "M. J. Electric, LLC", "M. J. Electric", "美国", "MI", "Iron Mountain", "mjelectric.com",
     "For more than six decades, M. J. Electric, a Quanta Services company, has performed comprehensive electrical construction in the electric transmission, substation, distribution, renewable energy, power, industrial, instrumentation, and civil/foundation sectors. As a multi-faceted ELECTRICAL CONTRACTOR, M. J. Electric can deliver comprehensive construction services through every phase of a project.", "⭐", "定向检索 substation high voltage electrical contractor Michigan", "✅ 入选"],
    ["292", "A 电气承包商/工程公司", "SCS Transmission Services LLC", "SCS Transmission", "美国", "SC", "York", "scstsllc.com",
     "SCS Transmission Services proudly serves the North and South Carolina region as a leading substation engineering company. Our crew is equipped to handle a variety of projects ranging from substation construction to transformer assembly and maintenance.", "⭐", "定向检索 substation construction electrical contractor Georgia North Carolina South Carolina", "✅ 入选"],
    ["293", "A 电气承包商/工程公司", "Gridco Inc", "Gridco", "美国", "AL", "Birmingham", "gridcompany.com",
     "Founded by utility executives, Gridco delivers infrastructure services across distribution, transmission, substation, fiber, and restoration. Today, Gridco serves major IOUs, cooperatives, and municipal utilities across the Southeast, Texas, and the Mid-Atlantic.", "⭐", "定向检索 substation construction electrical contractor Alabama utility contractor", "✅ 入选"],
    ["294", "A 电气承包商/工程公司", "D1 Substations", "D1 Substations", "美国", "PA", "Enola", "d1substations.com",
     "D1 Substations builds and maintains high-performance electrical substations with precision, safety, and reliability for utilities and contractors nationwide. We specialize in delivering end-to-end substation and high-voltage electrical infrastructure services with precision.", "⭐", "定向检索 substation electrical contractor Pennsylvania high voltage construction", "✅ 入选"],
    ["295", "A 电气承包商/工程公司", "Wright's Electric", "Wright's Electric", "美国", "PA", "Saylorsburg", "wrightselectric.net",
     "Wright's Electric is a specialized family owned High Voltage electrical contractor primarily serving northeast Pennsylvania and surrounding areas. EXPERTS IN ELECTRICAL DISTRIBUTION & TESTING. 服务含 Sub-Station Construction 与 Transformer Maintenance & Replacement。", "⭐", "定向检索 substation electrical contractor Pennsylvania high voltage construction", "✅ 入选"],
    ["296", "A 电气承包商/工程公司", "Vaughn Industries, Inc.", "Vaughn Industries", "美国", "OH", "Carey", "vaughnindustries.com",
     "Vaughn Industries is an Ohio based contractor delivering durable infrastructures tailored to the needs of Commercial, Institutional, and Industrial Clients. TRADES YOU NEED. PEOPLE YOU TRUST. — Electrical – Mechanical – High Voltage – Technology – Renewable Energy", "⭐", "定向检索 substation high voltage electrical contractor Ohio", "✅ 入选"],
    ["297", "A 电气承包商/工程公司", "Washington State Power LLC (WASP)", "WASP", "美国", "WA", "Olympia", "wastatepower.com",
     "WASP provides expert high voltage, telecommunications, and underground utility construction across the PNW. Proudly IBEW-affiliated. IBEW Union linemen specializing in overhead and underground distribution, transmission, and EV station infrastructure.", "⭐", "定向检索 high voltage transmission distribution contractor Washington", "✅ 入选"],
    ["298", "A 电气承包商/工程公司", "Aldridge Electric (Aldridge Group)", "Aldridge", "美国", "IL", "Libertyville", "aldridgegroup.com",
     "With nearly 75 years of experience completing the industry's most complex infrastructure projects, Aldridge is widely recognized as a leading electrical and foundation contractor in the United States. Markets include Substations and Transmission & Distribution.", "⭐", "定向检索 substation high voltage electrical contractor Illinois", "✅ 入选"],

    # ── B 类 · 加拿大 12 家（买家 299–310）───────────────────────────
    ["299", "B 分销商/贸易商", "Ideal Supply Inc.", "Ideal Supply", "加拿大", "ON", "Listowel", "idealsupply.com",
     "At Ideal Supply we stock only the highest quality electric supply products for residential, commercial and industrial contractors – from landscape lighting and range hoods to energy saving bulbs and industrial automation.", "—", "electricalindustry.ca 加拿大本土分销商名单", "✅ 入选"],
    ["300", "B 分销商/贸易商", "Paul Wolf Lighting & Electric Supply Ltd.", "Paul Wolf", "加拿大", "ON", "Toronto", "paulwolf.com",
     "Plug Into The Experts — Paul Wolf Lighting & Electric Supply Ltd, established in 1963. For all your electrical and lighting requirements.", "—", "electricalindustry.ca 加拿大本土分销商名单", "✅ 入选"],
    ["301", "B 分销商/贸易商", "House of Electrical Supplies Ltd.", "House of Electrical", "加拿大", "ON", "Markham", "houseofelectrical.com",
     "For over 45 years, House of Electrical Supplies has established itself as the place to come for exceptional service. As a proudly Canadian-owned and operated company, we are your one-stop shop for electrical supplies, automation, lighting solutions, cable assembly, and power distribution.", "—", "electricalindustry.ca 加拿大本土分销商名单", "✅ 入选"],
    ["302", "B 分销商/贸易商", "Oscan Electrical Supplies Ltd.", "Oscan", "加拿大", "ON", "Oshawa", "oscan.ca",
     "Oscan Electrical Supplies Ltd. Is a Canadian owned, independent wholesaler/distributor with a full line of industry leading electrical products from manufacturers you know and trust.", "—", "定向检索 electrical distributor Ontario", "✅ 入选"],
    ["303", "B 分销商/贸易商", "AC Nelson Electrical Ltd.", "AC Nelson", "加拿大", "BC", "Langley", "acnelson.com",
     "AC Nelson Electric is a proud Canadian family-owned business with over 50 years of experience providing electrical solutions. Our inventory includes products such as circuit breakers, transformers, switchgear, panels, disconnects, safety switches, and related electrical components.", "⭐", "定向检索 BC electrical distributor transformer", "✅ 入选"],
    ["304", "B 分销商/贸易商", "Sakura Distributors Inc.", "Sakura", "加拿大", "BC", "Abbotsford", "sakuracanada.com",
     "We are Electrical Distributors that server Canada's British Columbia Province with 5 different location. We carry all types of residential and commercial electrical supply. We cater to everyone, not just account holders.", "—", "poidata.io 省域电气批发商报告", "✅ 入选"],
    ["305", "B 分销商/贸易商", "First Choice Electrical Supply Ltd.", "First Choice", "加拿大", "AB", "Grande Prairie", "fcsupply.ca",
     "First Choice Electrical Supply Ltd. supplies parts to individuals and companies in the Peace River district of northwestern Alberta and northeastern British Columbia. We provide a lot of value added products for our customers, custom built panels, transformers, cords and lighting. We also provide an outlet for reconditioned parts.", "⭐", "ECAA 会员名录 — Distributor 分类", "✅ 入选"],
    ["306", "B 分销商/贸易商", "Deep Electrical Supply Ltd.", "Deep Electrical", "加拿大", "AB", "Edmonton", "deepelectricalsupply.com",
     "Canada's Fastest Growing Electrical Distributor — Deep Electrical Supply supports professional electrical work throughout Edmonton and across Canada. It offers circuit breakers and electrical panels for projects that involve distributing power safely and reliably.", "—", "定向检索 Alberta electrical distributor", "✅ 入选（替补 Mimecast 域）"],
    ["307", "B 分销商/贸易商", "SIB Électrique Inc.", "SIB Électrique", "加拿大", "QC", "Sherbrooke", "sibelectrique.com",
     "Vente, achat et location de matériel électrique industriel. Chez SIB Électrique, nous offrons une gamme complète d'équipements électriques industriels, allant des armoires de commutation aux transformateurs. Vous avez l'option d'effectuer un achat, une location et de développer un projet sur mesure. Nous achetons et revendons une vaste gamme de composantes électriques neuves et usagées.", "⭐", "定向检索 Quebec distributeur transformateur", "⚠️ 入选（制造线为开关柜/控制柜，与变压器互补）"],
    ["308", "B 分销商/贸易商（跨类：以变压器销售/租赁为主）", "Ligne STE", "Ligne STE", "加拿大", "QC", "Saint-Hyacinthe", "ligneste.com",
     "Ligne STE offre des solutions de vente, location et installation de transformateurs moyenne tension adaptées aux besoins des projets industriels, commerciaux et électriques partout au Québec. 产品含 sur socle（美变）/ sur poteau（柱上变）/ à l'huile（油浸）/ 单相 / 三相。", "⭐", "定向检索 transformateurs vente location Québec", "⚠️ 入选（跨类，兼营线路施工；供应商来源待核）"],
    ["309", "B 分销商/贸易商", "Location Power", "Location Power", "加拿大", "QC", "Boisbriand", "locationpower.ca",
     "Location de Transformateurs. Livraison partout au Québec. Location Power vous propose divers transformateurs basse et haute tension pouvant aller jusqu'à 600kVA et servir à différentes applications industrielles.", "⭐", "定向检索 location transformateurs Québec", "✅ 入选（邮件域为 powerrentals.ca）"],
    ["310", "B 分销商/贸易商", "Cape Nova Electrical Supplies Ltd.", "Cape Nova", "加拿大", "NS", "Port Hawkesbury", "capenova.ca",
     "Cape Nova Electrical Supplies Ltd is a locally owned and operated electrical supplier serving residential, commercial, and industrial customers. With over 50 years of combined experience. 产品分类：Distribution — Panels, breakers & transformers.", "⭐", "poidata.io Nova Scotia 电气批发商报告", "✅ 入选"],

    # ── B 类 · 美国 13 家（买家 311–323）─────────────────────────────
    ["311", "B 分销商/贸易商", "Transformers, Now!", "Transformers Now", "美国", "TX", "Carthage", "transformersnow.com",
     "Founded in 1999, Transformers, Now! is a family-owned and operated business with a passion for providing fast, reliable transformer solutions. Transformers, Now! specializes in providing fast-shipping solutions for both single-phase and three-phase distribution transformers, from 1kVA pole mounts to 40/50mVA substations. While we don't directly remanufacture transformers, our 25 years of industry experience have enabled us to forge strong partnerships with leading remanufacturers.", "⭐", "定向检索 power transformers for sale Texas", "✅ 入选"],
    ["312", "B 分销商/贸易商", "Greenville Transformer Company, Inc.", "Greenville Transformer", "美国", "TX", "Greenville", "greenvilletransformer.com",
     "Since 1961, Greenville Transformer Company has been the Southwest's premier supplier of new and reconditioned transformers. The 7-acre facility houses an extensive inventory of over 4,000 units, ranging from 5 KVA to 10,000 KVA, ready for immediate shipment.", "⭐", "定向检索 transformer supplier Southwest", "✅ 入选"],
    ["313", "B 分销商/贸易商", "Edison Electrical Surplus", "Edison Surplus", "美国", "FL", "Riviera Beach", "edisonelectricalsurplus.com",
     "At Edison Electrical Surplus, we supply the online world with circuit breakers and other electrical equipment at the lowest prices you'll find. We stock dry type transformers up to 500KVA in almost any voltage.", "⭐", "Electrical Advertiser 变压器经销商名录", "✅ 入选"],
    ["314", "B 分销商/贸易商", "Power Circuit Breakers LLC", "Power Circuit Breakers", "美国", "FL", "Plantation", "powercircuitbreakerss.com",
     "We are a growing company with 5 years of experience in the electrical equipment market. We provide a wide variety of electrical circuit breakers and electrical equipment. WE BUY ALL TYPES OF BRANDS OF ELECTRICAL EQUIPMENT — Circuit Breakers / Switch Gears / Bus Plugs / Motor Control / MCC / Panel Boards / Busway Switches / Transformers.", "⭐", "Electrical Advertiser 变压器经销商名录", "✅ 入选"],
    ["315", "B 分销商/贸易商", "Transcon of Michigan", "Transcon of Michigan", "美国", "MI", "Hamtramck", "transconofmichigan.com",
     "Large inventory of new, used and reconditioned high voltage disconnect switches and transformers in stock and ready to go. Sizes ranging from 200KVA-2500KVA. Specializing in wholesale to electrical contractors.", "⭐", "定向检索 transformer wholesale Michigan", "✅ 入选"],
    ["316", "B 分销商/贸易商", "Midwest Switchgear Division (Midwest Electrical Testing & Maintenance Co., Inc.)", "Midwest Switchgear", "美国", "WI", "Menomonee Falls", "swgr.com",
     "MIDWEST, YOUR HELPFUL CHOICE for reconditioned, used, obsolete and new electrical circuit breakers, transformers, bus plugs, and switchgear. MIDWEST also specializes in: Used, Reconditioned, and Obsolete equipment — New & Used Circuit Breakers and Transformers — Equipment Rental.", "⭐", "Electrical Advertiser 变压器经销商名录", "✅ 入选"],
    ["317", "B 分销商/贸易商", "Phoenix Transformer & Supply", "Phoenix Transformer", "美国", "AZ", "Glendale", "phoenixtransformer.com",
     "Phoenix Transformer & Supply has served industrial MRO's and electrical contractors with a combined experience of over 70 years in the electrical industry. Stocking New, Job Ready, Tested & Warrantied: Transformers, Panelboards, Disconnects, Fuses, Breakers & More.", "⭐", "定向检索 transformer sales Phoenix AZ", "✅ 入选"],
    ["318", "B 分销商/贸易商", "Belyea Company", "Belyea", "美国", "PA", "Easton", "belyeapower.com",
     "Belyea Company carries an extensive stock of power transformers. Our transformer inventory consists of outdoor oil filled substation-type, compartmentalized padmount (NEMA 3R enclosure), as well as indoor and outdoor dry-type ranging from 100 KVA though 100,000 KVA and beyond. Our extensive inventory allows us the ability to ship equipment fast and more economically than new or rewound units.", "⭐", "Electrical Advertiser 变压器经销商名录 + 定向检索", "✅ 入选（本批最对口：明示油浸 padmount + substation 型库存）"],
    ["319", "B 分销商/贸易商", "Voyten Electric & Electronics, Inc.", "Voyten Electric", "美国", "PA", "Polk", "voytenelectric.com",
     "Voyten Electric is a specialized industrial and commercial electrical wholesaler who offers new and reconditioned electrical equipment including electrical switchgear, circuit breakers, contact kits, electromagnetic coils and more. Whether you need obsolete electrical products that are hard to find or you need to rent an electrical product temporarily, we offer a wide variety of new, surplus, and obsolete electrical products.", "⭐", "定向检索 electrical wholesaler new reconditioned transformers", "✅ 入选"],
    ["320", "B 分销商/贸易商", "Row Electrical Equipment, Inc.", "Row Electrical", "美国", "OH", "Toledo", "rowelectrical.com",
     "Row Electrical Equipment, Inc., can address all of your electrical equipment requirements, including A.C. and D.C. motors, motor controls, transformers, power distribution, and switchgear. We buy and sell new and used industrial equipment throughout the United States plus companies in other countries. We inventory a wide variety of electric motors, motor controls, and transformers in our 100,000 Sq. Ft. Toledo warehouse.", "⭐", "定向检索 electrical equipment buy sell transformers Ohio", "✅ 入选"],
    ["321", "B 分销商/贸易商", "Bay Power", "Bay Power", "美国", "CA", "Modesto", "baypower.com",
     "Bay Power brings short lead times, extensive inventory, real in-house project expertise, and in-house service and testing together to help electrical contractors and maintenance professionals solve critical power problems fast. A vast inventory of top transformers and electrical components.", "⭐", "定向检索 transformer distributor California", "✅ 入选"],
    ["322", "B 分销商/贸易商", "Atlas Electric, Inc.", "Atlas Electric", "美国", "WA", "Spokane Valley", "atlaselectricinc.com",
     "Atlas Electric stocks hundreds of new, used, surplus and, reconditioned transformers. We are also OEM suppliers and distributors for several of the world's leading manufacturers and can provide the transformer you need for virtually any application.", "⭐", "Electrical Advertiser 变压器经销商名录", "✅ 入选"],
    ["323", "B 分销商/贸易商", "Dykman Electrical, Inc.", "Dykman", "美国", "ID", "Boise", "dykman.com",
     "For years we have been known to stock North America's largest inventory of electric motors, drives, controls, and reducers. Now, we also stock transformers and offer custom built UL508A panels—backed by knowledgeable sales professionals located across the U.S.", "⭐", "定向检索 electrical distributor transformer Denver Phoenix", "✅ 入选"],
]

# 剔除与备选（同样落盘，供替换）
EXTRA = [
    ["—", "⛔ ⓪层排除", "IronCore Global Resources Inc.", "IronCore", "加拿大", "BC", "Vancouver", "ironcoregr.com",
     "Transformer Solution Provider and Distributor. Engineered Transformer Solutions for Demanding Projects. Strong production capacity and organized supply support.", "—", "定向检索 BC transformer distributor", "⛔ 剔除（中国货源→北美通道）"],
    ["—", "⛔ 集团重复", "Choice Electrical Supply Co.", "Choice Supply", "加拿大", "SK", "Regina", "choicesupply.ca",
     "Choice Electrical Supply is an electrical distributor proudly serving Saskatchewan and Manitoba since 2001. Choice Electrical Supply is a division of Guillevin.", "—", "定向检索 Saskatchewan electrical distributor", "⛔ 剔除（Guillevin 分部，Guillevin 已在基线）"],
    ["—", "备选", "EHV Power Corporation", "EHV Power", "加拿大", "ON", "Gormley", "ehvpower.com",
     "EHV Power is a North American leader in high voltage underground transmission cable services (69 to 345 kV), specialized in oil-filled cable systems.", "⭐", "定向检索 high voltage underground transmission contractor Canada", "🔁 备选"],
    ["—", "备选", "Advanced Powerlines Ltd.", "Advanced Powerlines", "加拿大", "BC", "Kelowna", "advancedpowerlines.ca",
     "Advanced Powerlines is a full-service provider of distribution systems from 120 to 230,000 volts.", "⭐", "定向检索 BC powerline transmission contractor", "🔁 备选"],
    ["—", "备选", "Hardline Engineering", "Hardline", "加拿大", "AB", "Calgary", "hardlineeng.com",
     "From designing to developing, see our expertise that powers progress on overhead transmission lines from 69 kV to 500 kV. We design electric power facilities ranging from 4.16 kV to 500 kV.", "⭐", "定向检索 Alberta high voltage power engineering", "🔁 备选（与已建档 Firefly Power & Energy 为姐妹公司）"],
    ["—", "备选", "Noreaster Power Services", "Noreaster", "加拿大", "NS", "Onslow Mountain", "noreasterpower.com",
     "NOREASTER Power Services has your solutions to engineering, procurement, construction, and maintenance for all of your substation needs.", "⭐", "定向检索 Nova Scotia utility substation contractor", "🔁 备选"],
    ["—", "备选", "Gagnon Line Construction", "Gagnon Line", "加拿大", "NB", "Saint-André", "gagnonline.com",
     "Gagnon Line Construction is your trusted partner for high voltage electrical contracting and storm restoration across New Brunswick and Quebec.", "⭐", "定向检索 New Brunswick high voltage contractor", "🔁 备选"],
    ["—", "备选", "JSM Electrical Ltd.", "JSM Electrical", "加拿大", "NL", "St. John's", "jsmelectrical.ca",
     "JSM Electrical is a leading electrical and instrumentation contractor in Eastern Canada. Since 1982, our skilled professionals have delivered exceptional results across projects including industrial facilities, substations, and underground high and medium-voltage systems.", "⭐", "NLCA 会员名录 — Electrical Contractor 分类", "🔁 备选"],
    ["—", "备选", "Jomar Electrical Contractors", "Jomar", "美国", "TX", "Houston", "jomarinc.com",
     "When it comes to high voltage electrical infrastructure, Jomar is the go-to choice for top-quality work in energy renewables, storm response, and distribution.", "⭐", "Centex IEC 会员名录 + 定向检索", "🔁 备选"],
    ["—", "备选", "MasTec, Inc.", "MasTec", "美国", "FL", "Coral Gables", "mastec.com",
     "Leading specialty contractor engineers, designs and constructs infrastructures for electric power generation and transmission, oil and natural gas pipelines, renewable energy facilities and wireless networks.", "⭐", "定向检索 substation electrical contractor power delivery", "🔁 备选（超大型上市公司）"],
    ["—", "备选", "Pieper Electric, Inc.", "Pieper Electric", "美国", "WI", "Milwaukee", "pieperpower.com",
     "Pieper Electric delivers comprehensive electrical, mechanical, and automation services with 75+ years of experience. Full-Service Electrical, Mechanical & Automation Contractor.", "—", "定向检索 electrical contractor Wisconsin", "🔁 备选"],
    ["—", "备选", "Encore Electric, Inc.", "Encore Electric", "美国", "CO", "Lakewood", "encoreelectric.com",
     "Encore Electric is the premier electrical contractor, performing work in commercial, healthcare, data centers and more.", "—", "定向检索 electrical contractor substation Colorado", "🔁 备选"],
    ["—", "备选", "Canyon State Electric, Inc.", "Canyon State", "美国", "AZ", "Tempe", "canyonstateelectric.com",
     "Canyon State Electric is a trusted Arizona electrical contractor delivering electrical construction, design-build, low voltage, and maintenance services for healthcare, aviation, and mission-critical facilities.", "—", "定向检索 electrical contractor design-build Arizona", "🔁 备选"],
    ["—", "备选", "Wasatch Electric", "Wasatch Electric", "美国", "UT", "Salt Lake City", "wasatchelectric.com",
     "Wasatch Electric, a subsidiary of EMCOR Group, is a leading electrical contractor providing electrical construction design build services in Salt Lake City, Utah.", "—", "定向检索 electrical contractor design build Utah", "🔁 备选"],
    ["—", "备选", "Northwest High-Voltage Services, Inc.", "NW High-Voltage", "美国", "WA", "Benton City", "nwhighvoltage.com",
     "Northwest High-Voltage Services is a dependable Electrical Maintenance, Construction, and Engineering Services provider. We serve electrical utility companies in the states of Washington, Oregon, and Idaho.", "⭐", "定向检索 electrical contractor substation Oregon Washington Idaho", "🔁 备选"],
    ["—", "备选", "Western Equipment Limited", "Western Equipment", "加拿大", "ON", "Chatham", "westernequipment.com",
     "Biggest inventory in Chatham-Kent for the electrical supplies you need today! Western Equipment has served Southwestern Ontario for 80 years.", "—", "定向检索 electrical distributor Ontario", "🔁 备选"],
    ["—", "备选", "Lenmark Industries", "Lenmark", "加拿大", "BC", "Langley", "lenmark.com",
     "Lenmark connects serious buyers with trusted sellers through an industrial marketplace built for the realities of the job. A New Way to Buy Used.", "—", "poidata.io BC 电气批发商报告", "🔁 备选（二手工业品平台）"],
    ["—", "备选", "Dubo Électrique Ltée", "Dubo", "加拿大", "QC", "Québec City", "dubo.ca",
     "Since 1955, Dubo has been a leading distributor of electrical and lighting supplies across Quebec. With our branch network and dedicated experts, we empower contractors and professionals with reliable solutions, personalized service, and top-tier inventory.", "—", "定向检索 Quebec electrical distributor", "🔁 备选"],
    ["—", "备选", "Bernie's Electric Supplies Ltd.", "Bernie's", "加拿大", "AB", "Edmonton", "bernieselectric.ca",
     "Bernie's Electric Supplies is an independent electrical wholesaler based in Edmonton, Alberta. We serve large and small electrical contractors in the industrial, commercial, and residential sectors and we supply electrical components to OEMs.", "—", "ECAA 会员名录 — Distributor 分类", "🔁 备选（MX 走 Mimecast，项目有 PBL 拦截史）"],
    ["—", "备选", "Electrical Wholesalers (Calgary) Ltd.", "EWC", "加拿大", "AB", "Calgary", "electricalwholesalers.com",
     "Electrical Wholesalers (Calgary) Ltd. is a privately owned and operated electrical distributor servicing mainly the Calgary and Southern Alberta residential, commercial and industrial markets. Established in 1981.", "—", "ECAA 会员名录 — Distributor 分类", "🔁 备选（官网域无 MX，邮件域为 ewcl.net）"],
    ["—", "备选", "Causeway Electrical Supplies Ltd.", "Causeway", "加拿大", "NS", "Port Hawkesbury", "causewayelectrical.ca",
     "Causeway Electrical Supplies Ltd is an independent electrical supplier based in Port Hawkesbury, Nova Scotia. Established in 1983. We serve large and small electrical contractors in the industrial, commercial and residential sectors.", "—", "定向检索 Nova Scotia electrical wholesaler", "🔁 备选"],
    ["—", "备选", "B. A. Robinson Co. Ltd.", "Robinson Supply", "加拿大", "MB", "Winnipeg", "barobinson.com",
     "Robinson Supply is a fully diversified distributor of plumbing, HVAC, lighting and electrical products in Western Canada. We offer electrical and commercial lighting products in Saskatchewan, Manitoba, and Northwestern Ontario.", "—", "定向检索 Manitoba electrical distributor", "🔁 备选（主业 plumbing/HVAC，优先级低）"],
    ["—", "备选", "J&J Transformers LLC", "J&J Transformers", "美国", "TX", "Sugar Land", "jjtransformers.co",
     "J&J Transformers LLC buys, sells, and sources new, unused, surplus, and canceled-project industrial power equipment from Sugar Land, Texas.", "⭐", "定向检索 power transformers for sale Texas", "🔁 备选（域无 MX）"],
    ["—", "备选", "Salinger Electric Co., Inc.", "Salinger", "美国", "MI", "Troy", "salingerelectric.com",
     "Salinger Electric Co., Inc. has been selling quality electrical equipment both new and reconditioned since 1946. We can supply all new, all reconditioned, or a combination of electrical equipment and supplies at very competitive prices.", "—", "Electrical Advertiser 变压器经销商名录", "🔁 备选"],
    ["—", "备选", "American West Surplus LLC", "American West", "美国", "CO", "Denver", "americanwestsurplus.com",
     "We are a fast-growing supplier of commercial and industrial power distribution equipment. Transformers — OEM products in all major brands — New and Refurbished — Single and Three Phase — Dry type up to 500 KVA — Can order Pad Mounts and Specialty builds in any size.", "⭐", "Electrical Advertiser 变压器经销商名录", "⚠️ 备选（回收侧明示不收油浸，与销售侧口径冲突）"],
    ["—", "备选", "Current Electrical Supply", "Current Electrical", "美国", "GA", "Atlanta", "currentga.com",
     "Electrical Supplies for the Atlanta Market. Our Team has more than 30 years of experience in the Atlanta Electrical Distribution Market.", "—", "定向检索 electrical distributor Atlanta transformer", "🔁 备选"],
    ["—", "备选", "Holder Electric Supply, Inc.", "Holder Electric", "美国", "SC", "Greenville", "holderelectric.com",
     "At Holder Electric Supply, we strive to be your first choice when you are looking to partner with an electrical distributor. Please keep in mind that we are an electrical distributor, not an electrical contractor.", "—", "定向检索 electrical distributor Greenville SC", "🔁 备选"],
    ["—", "备选", "Select Equipment Co.", "Select Equipment", "美国", "IN", "Kokomo", "selectequipment.net",
     "Select Equipment Co. stocks all types of new and reconditioned electrical transformers for sale. From large industrial transformers to… Refurbished, retrofitted, reconditioned industrial electrical supplies, machine controls.", "⭐", "Electrical Advertiser 变压器经销商名录", "🔁 备选"],
    ["—", "备选", "Allteck Line Contractors Ltd.", "Allteck", "加拿大", "BC", "Surrey", "allteck.com",
     "（官网原文未取证；已知业务含 transmission / distribution / substations，Quanta Services 旗下）", "⭐", "定向检索 BC powerline contractor", "⚠️ 疑似假阳性（被基线短词 k line 命中），需取证官网原文后再定"],
]

out = BASE / "目标客户清单-batch8.csv"
with out.open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f)
    w.writerow(HDR)
    w.writerows(ROWS)
    w.writerows(EXTRA)

sel = [r for r in ROWS]
from collections import Counter
print(f"写出 -> {out}")
print(f"入选 {len(sel)} 家 ｜ 附加（剔除+备选） {len(EXTRA)} 行 ｜ 合计 {len(ROWS)+len(EXTRA)+1} 行")
print("\n--- 入选构成 ---")
print("类型:", dict(Counter(r[1].split('（')[0] for r in sel)))
print("国家:", dict(Counter(r[4] for r in sel)))
print("州省:", dict(Counter(f"{r[4]}-{r[5]}" for r in sel)))
print("⭐ 高价值:", sum(1 for r in sel if r[9] == "⭐"), "/", len(sel))
