from pathlib import Path

root = Path(r"C:/Users/阿镇/website")
source = (root / "index.html").read_text(encoding="utf-8")


def apply_replacements(text: str, replacements):
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def build_tw():
    text = source
    replacements = [
        ('<html lang="zh-CN">', '<html lang="zh-TW">'),
        ('<title>FrostVend - 重新定义冰淇淋零售 | 全世界首创挂式冰淇淋自动售货机</title>', '<title>FrostVend - 重新定義冰淇淋零售 | 全世界首創掛式冰淇淋自動售貨機</title>'),
        ('<meta name="description" content="全世界首创挂式陈列冰淇淋自动售货机。超低故障率0.1%、连续出货30支、600支大容量、50个单品、超低能耗、箱体无霜。">', '<meta name="description" content="全世界首創掛式陳列冰淇淋自動售貨機。超低故障率0.1%、連續出貨30支、600支大容量、50個單品、超低能耗、箱體無霜。">'),
        ('<meta name="keywords" content="冰淇淋自动售货机,挂式陈列,雪糕机,无人售货,创新设备">', '<meta name="keywords" content="冰淇淋自動售貨機,掛式陳列,雪糕機,無人售貨,創新設備">'),
        ('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="../css/style.css">'),
        ('<div class="lang-switcher">\n        <span class="lang-current">简体</span>\n        <a href="tw/index.html" class="lang-btn">繁体</a>\n        <a href="en/index.html" class="lang-btn">English</a>\n        <a href="ja/index.html" class="lang-btn">日本語</a>\n        <a href="ko/index.html" class="lang-btn">한국어</a>\n    </div>', '<div class="lang-switcher">\n        <a href="../index.html" class="lang-btn">简体</a>\n        <span class="lang-current">繁體</span>\n        <a href="../en/index.html" class="lang-btn">English</a>\n        <a href="../ja/index.html" class="lang-btn">日本語</a>\n        <a href="../ko/index.html" class="lang-btn">한국어</a>\n    </div>'),
        ('首页', '首頁'), ('特点', '特點'), ('产品', '產品'), ('购买', '購買'), ('场景', '場景'), ('联系', '聯繫'),
        ('全世界首创', '全世界首創'),
        ('挂式雪糕自动售货机', '掛式雪糕自動售貨機'),
        ('全世界首创挂式陈列冰淇淋自动售货机', '全世界首創掛式陳列冰淇淋自動售貨機'),
        ('颠覆传统卧式冰柜，开启智能零售新时代', '顛覆傳統臥式冰櫃，開啟智能零售新時代'),
        ('个单品陈列', '個單品陳列'), ('支连续出货', '支連續出貨'), ('超低卡货率', '超低卡貨率'), ('度电/天(户外)', '度電/天(戶外)'), ('整体无霜', '整體無霜'),
        ('了解特点', '了解特點'),
        ('八大核心特点', '八大核心特點'), ('每一项都是颠覆行业的创新', '每一項都是顛覆行業的創新'),
        ('挂式陈列', '掛式陳列'), ('所有商品悬挂式整齐陈列，顾客通过真空玻璃直观看到所有雪糕', '所有商品懸掛式整齊陳列，顧客透過真空玻璃直觀看到所有雪糕'),
        ('首创', '首創'), ('悬挂挂载商品，接触面积小，无水汽粘连，故障率≤0.1%', '懸掛掛載商品，接觸面積小，無水汽黏連，故障率≤0.1%'),
        ('独家', '獨家'), ('连续出货30支', '連續出貨30支'), ('一次性购买30支雪糕，连续出货，故障率≤0.1%', '一次性購買30支雪糕，連續出貨，故障率≤0.1%'),
        ('50个货道，每道12支，满载600支库存容量', '50個貨道，每道12支，滿載600支庫存容量'),
        ('50个单品陈列', '50個單品陳列'), ('可陈列50个单品，满足顾客多样性需求', '可陳列50個單品，滿足顧客多樣性需求'),
        ('户外单日耗电10-12度，与卧式冰柜耗电量相同', '戶外單日耗電10-12度，與臥式冰櫃耗電量相同'),
        ('无霜箱体', '無霜箱體'), ('风冷制冷技术，箱体无霜，干净整洁', '風冷製冷技術，箱體無霜，乾淨整潔'),
        ('模块化结构', '模組化結構'), ('制冷机组、箱体、出货结构三大模块，可整体更换，降低维护成本', '製冷機組、箱體、出貨結構三大模組，可整體更換，降低維護成本'),
        ('专利认证 · 原创保障', '專利認證 · 原創保障'), ('多项国家专利，技术原创保障', '多項國家專利，技術原創保障'),
        ('实用新型专利', '實用新型專利'), ('外观设计专利', '外觀設計專利'), ('螺旋悬挂货道', '螺旋懸掛貨道'), ('螺旋悬挂式雪糕自动售货机', '螺旋懸掛式雪糕自動售貨機'), ('螺旋悬挂货道结构', '螺旋懸掛貨道結構'), ('自动售货机出货结构', '自動售貨機出貨結構'),
        ('颠覆传统 · 重新定义', '顛覆傳統 · 重新定義'), ('全面对比', '全面對比'), ('陈列方式', '陳列方式'), ('挂式陈列，品牌直观展示', '掛式陳列，品牌直觀展示'), ('卡式陈列，东倒西歪', '卡式陳列，東倒西歪'), ('卧式平躺，整体凌乱', '臥式平躺，整體凌亂'),
        ('单品数量', '單品數量'), ('50个单品', '50個單品'), ('40个单品', '40個單品'), ('10-20个单品', '10-20個單品'),
        ('运营方式', '運營方式'), ('24小时无人自助', '24小時無人自助'), ('24小时自助', '24小時自助'), ('需要人工值守', '需要人工值守'),
        ('户外能耗', '戶外能耗'), ('约10-12度电/天', '約10-12度電/天'), ('12-18度电/天', '12-18度電/天'), ('15-20度电/天', '15-20度電/天'), ('12-15度电/天', '12-15度電/天'),
        ('维护成本', '維護成本'), ('模块化设计，快速维护', '模組化設計，快速維護'), ('需专业维修人员', '需專業維修人員'), ('安全隐患，易损失', '安全隱患，易損失'), ('需人工除霜', '需人工除霜'),
        ('箱体状况', '箱體狀況'), ('无霜设计，干净整洁', '無霜設計，乾淨整潔'), ('无霜，但不整洁', '無霜，但不整潔'), ('需要人工除霜', '需要人工除霜'),
        ('故障率', '故障率'), ('悬挂式结构故障率≤0.1%', '懸掛式結構故障率≤0.1%'), ('接触面大，卡货率高', '接觸面大，卡貨率高'), ('识别不准，故障频发', '識別不準，故障頻發'), ('人工结账误差≤1%', '人工結帳誤差≤1%'),
        ('连续出货', '連續出貨'), ('一次性出30支雪糕故障率≤0.1%', '一次性出30支雪糕故障率≤0.1%'), ('一次出货5支以上故障率翻倍', '一次出貨5支以上故障率翻倍'), ('识别准确率低', '識別準確率低'), ('人工误差 ≤1%', '人工誤差 ≤1%'),
        ('密封性', '密封性'), ('密封性优异，连续出货箱体温度变化不大', '密封性優異，連續出貨箱體溫度變化不大'), ('整体密封好', '整體密封好'), ('反复开门冷气泄漏严重，会导致雪糕融化', '反覆開門冷氣洩漏嚴重，會導致雪糕融化'),
        ('标价', '標價'), ('明码标价', '明碼標價'), ('没有标价', '沒有標價'), ('综合评分', '綜合評分'), ('较差', '較差'),
        ('产品展示', '產品展示'), ('全方位查看产品细节', '全方位查看產品細節'), ('产品细节', '產品細節'), ('应用场景', '應用場景'),
        ('机场', '機場'), ('高校', '高校'), ('街头', '街頭'), ('医院', '醫院'), ('工厂', '工廠'), ('公园', '公園'), ('景区', '景區'), ('校园', '校園'), ('商场', '商場'), ('地铁', '地鐵'), ('社区', '社區'), ('海边', '海邊'), ('乐园', '樂園'), ('楼宇', '樓宇'),
        ('产品规格', '產品規格'), ('尺寸', '尺寸'), ('电压', '電壓'), ('功率', '功率'), ('货道数', '貨道數'), ('单道容量', '單道容量'), ('总容量', '總容量'), ('制冷温度', '製冷溫度'), ('出货速度', '出貨速度'), ('卡货率', '卡貨率'), ('箱体技术', '箱體技術'),
        ('简单4步，便捷购买', '簡單4步，便捷購買'), ('无需下载APP，微信扫码即可购买', '無需下載APP，微信掃碼即可購買'), ('扫码', '掃碼'), ('微信扫一扫', '微信掃一掃'), ('选品', '選品'), ('最多选30支', '最多選30支'), ('线上支付', '線上支付'), ('冰淇淋掉落', '冰淇淋掉落'),
        ('多种合作方式', '多種合作方式'), ('灵活共赢，共创未来', '靈活共贏，共創未來'), ('区域代理', '區域代理'), ('设备采购', '設備採購'), ('技术合作', '技術合作'), ('为品牌商定制生产', '為品牌商定制生產'), ('区域独家代理', '區域獨家代理'), ('直接采购设备', '直接採購設備'), ('技术授权/合资', '技術授權/合資'), ('详情面谈', '詳情面談'), ('合作模式面谈', '合作模式面談'), ('立即咨询', '立即咨詢'), ('合作流程', '合作流程'), ('商务洽谈', '商務洽談'), ('实地考察', '實地考察'), ('签订合同', '簽訂合同'), ('设备交付', '設備交付'), ('上线运营', '上線運營'),
        ('联系我们', '聯繫我們'), ('期待与您合作', '期待與您合作'), ('填写合作意向', '填寫合作意向'), ('请输入您的姓名', '請輸入您的姓名'), ('电话 *', '電話 *'), ('请输入联系电话', '請輸入聯繫電話'), ('公司/团队', '公司/團隊'), ('请输入公司或团队名称', '請輸入公司或團隊名稱'), ('合作类型 *', '合作類型 *'), ('请选择', '請選擇'), ('请输入所在城市', '請輸入所在城市'), ('请输入您的需求或问题', '請輸入您的需求或問題'), ('联系方式', '聯繫方式'), ('电话', '電話'), ('邮箱', '郵箱'), ('扫码添加微信', '掃碼添加微信'),
        ('关于FrostVend', '關於 FrostVend'), ('核心特点', '核心特點'), ('© 2026 成都智草网络科技有限公司 版权所有', '© 2026 成都智草網絡科技有限公司 版權所有'),
        ('src="images/', 'src="../images/'), ('href="images/', 'href="../images/'), ('<script src="js/script.js"></script>', '<script src="../js/script.js"></script>')
    ]
    return apply_replacements(text, replacements)


def build_en():
    text = source
    replacements = [
        ('<html lang="zh-CN">', '<html lang="en">'),
        ('<title>FrostVend - 重新定义冰淇淋零售 | 全世界首创挂式冰淇淋自动售货机</title>', '<title>FrostVend - Reinventing Ice Cream Retail | World\'s First Hanging Ice Cream Vending Machine</title>'),
        ('<meta name="description" content="全世界首创挂式陈列冰淇淋自动售货机。超低故障率0.1%、连续出货30支、600支大容量、50个单品、超低能耗、箱体无霜。">', '<meta name="description" content="The world\'s first hanging-display ice cream vending machine. Ultra-low failure rate 0.1%, 30 consecutive dispenses, 600-item capacity, 50 SKUs, ultra-low energy consumption, and a frost-free cabinet.">'),
        ('<meta name="keywords" content="冰淇淋自动售货机,挂式陈列,雪糕机,无人售货,创新设备">', '<meta name="keywords" content="ice cream vending machine,hanging display,ice cream machine,unattended vending,innovative equipment">'),
        ('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="../css/style.css">'),
        ('<div class="lang-switcher">\n        <span class="lang-current">简体</span>\n        <a href="tw/index.html" class="lang-btn">繁体</a>\n        <a href="en/index.html" class="lang-btn">English</a>\n        <a href="ja/index.html" class="lang-btn">日本語</a>\n        <a href="ko/index.html" class="lang-btn">한국어</a>\n    </div>', '<div class="lang-switcher">\n        <a href="../index.html" class="lang-btn">简体</a>\n        <a href="../tw/index.html" class="lang-btn">繁體</a>\n        <span class="lang-current">English</span>\n        <a href="../ja/index.html" class="lang-btn">日本語</a>\n        <a href="../ko/index.html" class="lang-btn">한국어</a>\n    </div>'),
        ('首页', 'Home'), ('特点', 'Features'), ('产品', 'Product'), ('购买', 'Purchase'), ('场景', 'Scenes'), ('合作', 'Cooperation'), ('联系', 'Contact'),
        ('全世界首创', 'WORLD\'S FIRST'), ('挂式雪糕自动售货机', 'Hanging Ice Cream Vending Machine'),
        ('全世界首创挂式陈列冰淇淋自动售货机', 'The world\'s first hanging-display ice cream vending machine'),
        ('颠覆传统卧式冰柜，开启智能零售新时代', 'Disrupting traditional chest freezers and opening a new era of smart retail'),
        ('支容量', 'Capacity'), ('个单品陈列', 'SKU Display'), ('支连续出货', 'Consecutive Dispense'), ('超低卡货率', 'Ultra-Low Jam Rate'), ('度电/天(户外)', 'kWh/day (Outdoor)'), ('整体无霜', 'Frost-Free'),
        ('立即合作', 'Cooperate Now'), ('了解特点', 'Explore Features'),
        ('八大核心特点', 'Eight Core Advantages'), ('每一项都是颠覆行业的创新', 'Every point is a category-disrupting innovation'),
        ('挂式陈列', 'Hanging Display'), ('所有商品悬挂式整齐陈列，顾客通过真空玻璃直观看到所有雪糕', 'All products are neatly displayed in hanging form, and customers can clearly view every ice cream through the vacuum glass'),
        ('首创', 'First-in-Class'), ('超低故障率', 'Ultra-Low Failure Rate'), ('悬挂挂载商品，接触面积小，无水汽粘连，故障率≤0.1%', 'The hanging structure minimizes contact area, avoids moisture adhesion, and keeps the failure rate at ≤0.1%'),
        ('独家', 'Exclusive'), ('连续出货30支', '30 Consecutive Dispenses'), ('一次性购买30支雪糕，连续出货，故障率≤0.1%', 'Customers can buy 30 ice creams at once with consecutive dispensing and a failure rate of ≤0.1%'),
        ('600支大容量', '600-Item Capacity'), ('50个货道，每道12支，满载600支库存容量', '50 lanes with 12 items each, providing a full loaded capacity of 600 ice creams'),
        ('50个单品陈列', '50 SKU Display'), ('可陈列50个单品，满足顾客多样性需求', 'Displays up to 50 SKUs to meet diverse customer needs'),
        ('超低能耗', 'Ultra-Low Energy Use'), ('户外单日耗电10-12度，与卧式冰柜耗电量相同', 'Outdoor daily power use is only 10–12 kWh, the same as a chest freezer'),
        ('无霜箱体', 'Frost-Free Cabinet'), ('风冷制冷技术，箱体无霜，干净整洁', 'Air-cooling technology keeps the cabinet frost-free, clean, and tidy'),
        ('模块化结构', 'Modular Structure'), ('制冷机组、箱体、出货结构三大模块，可整体更换，降低维护成本', 'The cooling unit, cabinet, and dispensing structure are three major modules that can be replaced as a whole to reduce maintenance costs'),
        ('专利认证 · 原创保障', 'Patent Protection · Original Innovation'), ('多项国家专利，技术原创保障', 'Multiple national patents protect the originality of the technology'),
        ('实用新型专利', 'Utility Model Patent'), ('外观设计专利', 'Design Patent'), ('螺旋悬挂货道', 'Spiral Hanging Lane'), ('螺旋悬挂式雪糕自动售货机', 'Spiral Hanging Ice Cream Vending Machine'), ('螺旋悬挂货道结构', 'Spiral Hanging Lane Structure'), ('自动售货机出货结构', 'Vending Machine Dispensing Structure'),
        ('颠覆传统 · 重新定义', 'Disrupt Tradition · Redefine'), ('全面对比', 'Comprehensive comparison'), ('陈列方式', 'Display Method'), ('挂式陈列，品牌直观展示', 'Hanging display with direct brand visibility'), ('卡式陈列，东倒西歪', 'Card-slot display, messy and tilted'), ('卧式平躺，整体凌乱', 'Flat chest display, visually cluttered'),
        ('单品数量', 'SKU Count'), ('50个单品', '50 SKUs'), ('40个单品', '40 SKUs'), ('10-20个单品', '10–20 SKUs'),
        ('运营方式', 'Operation Mode'), ('24小时无人自助', '24/7 unattended self-service'), ('24小时自助', '24/7 self-service'), ('需要人工值守', 'Requires on-site staff'),
        ('户外能耗', 'Outdoor Energy Use'), ('约10-12度电/天', 'About 10–12 kWh/day'), ('12-18度电/天', '12–18 kWh/day'), ('15-20度电/天', '15–20 kWh/day'), ('12-15度电/天', '12–15 kWh/day'),
        ('维护成本', 'Maintenance Cost'), ('模块化设计，快速维护', 'Modular design for fast maintenance'), ('需专业维修人员', 'Requires professional technicians'), ('安全隐患，易损失', 'Safety risks and easy losses'), ('需人工除霜', 'Needs manual defrosting'),
        ('箱体状况', 'Cabinet Status'), ('无霜设计，干净整洁', 'Frost-free, clean, and tidy'), ('无霜，但不整洁', 'Frost-free, but untidy'), ('需要人工除霜', 'Needs manual defrosting'),
        ('故障率', 'Failure Rate'), ('悬挂式结构故障率≤0.1%', 'Hanging structure failure rate ≤0.1%'), ('接触面大，卡货率高', 'Large contact area, high jam rate'), ('识别不准，故障频发', 'Inaccurate recognition, frequent faults'), ('人工结账误差≤1%', 'Manual checkout error ≤1%'),
        ('连续出货', 'Consecutive Dispense'), ('一次性出30支雪糕故障率≤0.1%', 'Failure rate ≤0.1% when dispensing 30 ice creams at once'), ('一次出货5支以上故障率翻倍', 'Failure rate doubles when dispensing more than 5 at once'), ('识别准确率低', 'Low recognition accuracy'), ('人工误差 ≤1%', 'Manual error ≤1%'),
        ('密封性', 'Sealing Performance'), ('密封性优异，连续出货箱体温度变化不大', 'Excellent sealing; cabinet temperature stays stable during continuous dispensing'), ('整体密封好', 'Overall sealing is good'), ('反复开门冷气泄漏严重，会导致雪糕融化', 'Repeated door opening causes severe cold-air leakage and may melt the ice cream'),
        ('标价', 'Pricing'), ('明码标价', 'Clearly marked pricing'), ('没有标价', 'No visible pricing'), ('综合评分', 'Overall Score'), ('完美', 'Excellent'), ('一般', 'Average'), ('较差', 'Poor'),
        ('产品展示', 'Product Showcase'), ('全方位查看产品细节', 'See product details from every angle'), ('产品细节', 'Product Details'), ('应用场景', 'Application Scenarios'),
        ('机场', 'Airport'), ('高铁', 'High-Speed Rail'), ('高校', 'University'), ('街头', 'Street'), ('医院', 'Hospital'), ('工厂', 'Factory'), ('公园', 'Park'), ('景区', 'Scenic Area'), ('校园', 'Campus'), ('商场', 'Shopping Mall'), ('地铁', 'Metro'), ('社区', 'Community'), ('海边', 'Seaside'), ('乐园', 'Amusement Park'), ('楼宇', 'Office Building'),
        ('产品规格', 'Specifications'), ('尺寸', 'Dimensions'), ('电压', 'Voltage'), ('功率', 'Power'), ('货道数', 'Lane Count'), ('单道容量', 'Per-Lane Capacity'), ('总容量', 'Total Capacity'), ('通信方式', 'Connectivity'), ('制冷温度', 'Cooling Temperature'), ('出货速度', 'Dispense Speed'), ('卡货率', 'Jam Rate'), ('陈列方式', 'Display Type'), ('箱体技术', 'Cabinet Technology'),
        ('简单4步，便捷购买', 'Simple 4-Step Purchase'), ('无需下载APP，微信扫码即可购买', 'No app download needed. Scan with WeChat to buy instantly'), ('扫码', 'Scan'), ('微信扫一扫', 'Scan with WeChat'), ('选品', 'Select'), ('最多选30支', 'Choose up to 30 items'), ('支付', 'Pay'), ('线上支付', 'Online Payment'), ('出货', 'Dispense'), ('冰淇淋掉落', 'Ice cream drops out'),
        ('多种合作方式', 'Multiple Cooperation Models'), ('灵活共赢，共创未来', 'Flexible win-win cooperation for a shared future'), ('区域代理', 'Regional Agency'), ('设备采购', 'Equipment Purchase'), ('技术合作', 'Technical Cooperation'), ('为品牌商定制生产', 'Customized production for brands'), ('区域独家代理', 'Exclusive regional agency'), ('直接采购设备', 'Direct equipment purchase'), ('技术授权/合资', 'Technology licensing / joint venture'), ('详情面谈', 'Discuss details'), ('合作模式面谈', 'Cooperation model by discussion'), ('立即咨询', 'Contact Now'), ('合作流程', 'Cooperation Process'), ('提交意向', 'Submit Intent'), ('商务洽谈', 'Business Discussion'), ('实地考察', 'Site Visit'), ('签订合同', 'Sign Contract'), ('设备交付', 'Equipment Delivery'), ('上线运营', 'Launch Operation'),
        ('联系我们', 'Contact Us'), ('期待与您合作', 'We look forward to working with you'), ('填写合作意向', 'Submit Cooperation Intent'), ('姓名 *', 'Name *'), ('请输入您的姓名', 'Please enter your name'), ('电话 *', 'Phone *'), ('请输入联系电话', 'Please enter your phone number'), ('公司/团队', 'Company / Team'), ('请输入公司或团队名称', 'Please enter your company or team name'), ('合作类型 *', 'Cooperation Type *'), ('请选择', 'Please Select'), ('所在城市', 'City'), ('请输入所在城市', 'Please enter your city'), ('留言', 'Message'), ('请输入您的需求或问题', 'Please enter your requirements or questions'), ('提交意向', 'Submit'), ('联系方式', 'Contact Information'), ('电话', 'Phone'), ('邮箱', 'Email'), ('扫码添加微信', 'Scan to add WeChat'),
        ('关于FrostVend', 'About FrostVend'), ('核心特点', 'Core Advantages'), ('合作方式', 'Cooperation Models'), ('全世界首创挂式冰淇淋自动售货机', 'The world\'s first hanging ice cream vending machine'), ('© 2026 成都智草网络科技有限公司 版权所有', '© 2026 Chengdu Zhicao Network Technology Co., Ltd. All rights reserved'),
        ('src="images/', 'src="../images/'), ('href="images/', 'href="../images/'), ('<script src="js/script.js"></script>', '<script src="../js/script.js"></script>')
    ]
    return apply_replacements(text, replacements)

(root / 'tw' / 'index.html').write_text(build_tw(), encoding='utf-8')
(root / 'en' / 'index.html').write_text(build_en(), encoding='utf-8')
print('updated tw and en')
