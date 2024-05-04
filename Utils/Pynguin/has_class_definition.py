import ast


def has_class_definition(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            return True
    return False


# file_path = "../../ProgramTobeTested/python_2024_04_20_13_52_01/buggy/Array_Collapse.txt"  # 修改为你想要检查的 Python 文件路径
# if has_class_definition(file_path):
#     print("The file defines at least one class.")
# else:
#     print("The file does not define any class.")
