import json


# 函数用于将字典追加写入 JSON 文件
def append_to_json(data, filename):
    try:
        # 尝试读取现有的 JSON 文件内容
        with open(filename, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        # 如果文件不存在，则创建一个空列表
        existing_data = []

    # 追加新的数据到列表中
    existing_data.append(data)

    # 将列表写入 JSON 文件
    with open(filename, 'w') as file:
        json.dump(existing_data, file, indent=4)


# obj_dict = {
#     "filename": "filename",
#     "iteration": "filename",
#     "input": "filename",
#     "expectedOutput": "filename"
# }
# # 追加字典到 JSON 文件
# current_time = "python_2024_04_21_11_40_01"
# append_to_json(obj_dict, f'./data/{current_time}/InAndOut.json')








