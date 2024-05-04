import os
import subprocess

from Utils.Pynguin.has_class_definition import has_class_definition


def run_all_pynguin(current_time):
    sourcecodedir = f"./ProgramTobeTested/{current_time}/buggy"
    # 检查目录是否存在
    if not os.path.isdir(sourcecodedir):
        print(f"Error: '{sourcecodedir}' is not a valid directory.")
        return

    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(sourcecodedir):
        for file in files:
            # 检查文件扩展名是否为 .py
            if file.endswith('.py'):
                filename = file[:-3]
                run_pynguin(filename, current_time)


def run_pynguin(filename, current_time):
    # 设置环境变量，强制使用UTF-8编码
    os.environ["PYTHONIOENCODING"] = "utf-8"

    commom_command = [
        "pynguin",
        "--project-path", f"./ProgramTobeTested/{current_time}/buggy",
        "--output-path", f"./Utils/Pynguin/data/{current_time}",
        "--module-name", filename,  # 使用函数参数指定的模块名
        "-v"
    ]
    class_command = [
        "pynguin",
        "--project-path", f"./ProgramTobeTested/{current_time}/buggy",
        "--output-path", f"./Utils/Pynguin/data/{current_time}",
        "--module-name", filename,  # 使用函数参数指定的模块名
        "-v",
        "--seed", "1629381673714481067"
    ]
    sourcecodepath = f"./ProgramTobeTested/{current_time}/buggy/{filename}.py"
    if has_class_definition(sourcecodepath):
        process = subprocess.Popen(class_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                   encoding='utf-8')
    else:
        process = subprocess.Popen(commom_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                   encoding='utf-8')

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())

    # 新功能的实现部分
    output_path = f"./Utils/Pynguin/data/{current_time}"  # 指定的输出路径
    # output_path = f"./Utils/Pynguin/data/{current_time}"  # 指定的输出路径
    prefix = f'from buggy '  # 要添加的前缀

    # 遍历output_path目录下的所有.py文件
    for root, dirs, files in os.walk(output_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                with open(file_path, 'w', encoding='utf-8') as f:
                    for line in lines:
                        # 检查是否包含指定的字符串
                        if 'module_0' in line and 'import' in line:
                            line = prefix + line  # 在行前添加指定的字符串
                        f.write(line)


# 使用示例
# run_pynguin("Array_Collapse","python_2024_04_20_13_52_01")
# run_pynguin("Game_with_Multiset","python_2024_04_20_13_52_01")
# run_pynguin("Matrix_Problem","python_2024_04_20_13_52_01")
# run_pynguin("Rating_Increase","python_2024_04_20_13_52_01")
# run_pynguin("Swap_and_Delete","python_2024_04_20_13_52_01")
# list_python_files("python_2024_04_20_13_52_01")
