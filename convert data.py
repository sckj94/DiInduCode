import json

# 读取data2.json文件
with open('data2.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

# 初始化一个空列表来存储转换后的数据
data = []

# 遍历data2.json的结构
for category, subcategories in data2.items():
    for subcategory, items in subcategories.items():
        for item in items:
            # 创建一个新的字典来存储转换后的数据
            new_item = {
                "生产性服务业大类": item.get("大类代码", ""),
                "生产性服务业大类名称": category,
                "生产性服务业中类": item.get("中类代码", ""),
                "生产性服务业中类名称": subcategory,
                "生产性服务业小类": item.get("小类代码", ""),
                "生产性服务业小类名称": item.get("小类名称", ""),
                "说明": item.get("小类说明", ""),
                "国民经济行业代码": item.get("国民经济行业代码", ""),
                "国民经济行业名称": ""  # 需要根据代码查找对应的名称
            }
            # 将新字典添加到列表中
            data.append(new_item)

# 将转换后的数据写入data.json文件
with open('data3.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
