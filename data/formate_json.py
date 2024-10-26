import json

# 读取JSON文件
with open('all_function.json', 'r') as file:
    data = json.load(file)

# 输出缩进的JSON到控制台
with open('all_function_indent.json', 'w') as file:
    json.dump(data, file, indent=4)