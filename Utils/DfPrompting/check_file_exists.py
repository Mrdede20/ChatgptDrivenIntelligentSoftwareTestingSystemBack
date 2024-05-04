import os

# 判断指定目录下的指定文件是否存在
def check_file_exists(directory, filename):
    # 构建完整的文件路径
    file_path = os.path.join(directory, filename)

    # 检查文件是否存在   
    if os.path.exists(file_path):
        print(f"File exists: {file_path}")
        return True
    else:
        print(f"File does not exist: {file_path}")
        return False


# # 使用示例
# directory = './data/python_2024_04_21_11_40_01/Monocarp'
# filename = 'PUT_code.py'
# exists = check_file_exists(directory, filename)
