import json

# 读取JSON文件
with open('train.json', 'r') as file:
    data = json.load(file)

# 输出缩进的JSON到控制台
with open('formatted_train.json', 'w') as file:
    json.dump(data, file, indent=4)