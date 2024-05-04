import ast


def has_specific_function(file_path, function_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            return True
    return False

# 使用示例
# current_time = "python_2024_04_16_18_30_40"
# file_path = "../../ProgramTobeTested/" + current_time + "/buggyFunction" + "/Array_Collapse.txt"
# function_name = "array_collapse"
# if has_specific_function(file_path, function_name):
#     print(f"'{file_path}' 文件中定义了名为 '{function_name}' 的函数。")
# else:
#     print(f"'{file_path}' 文件中没有定义名为 '{function_name}' 的函数。")
