import subprocess
# 这个用来运行未经过函数包装的程序


def subprocess_run_program(file_path, input_value):
    """
    使用 subprocess 模块运行一个指定的 Python 程序，并向其传递输入。

    参数:
    file_path (str): 要运行的 Python 文件的路径。
    input_value (str): 传递给 Python 程序的输入值。

    返回:
    output (str): 程序的输出。
    """
    # 启动子进程运行 Python 程序
    process = subprocess.Popen(['python', file_path],
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True)

    # 向程序传递 input_value，并获取输出
    output, errors = process.communicate(input=input_value)

    # 检查是否有错误发生
    if process.returncode != 0:
        print(f"Error running program: {errors}")
        return errors
    return output

# # 示例用法
# path = "../../ProgramTobeTested/python_2024_04_16_18_30_40/buggy/Array_Collapse.txt"  # 这里填写你的 Python 文件路径
# user_input = "2\n5\n1 2 3 4 5\n4\n5 4 3 2"  # 这里填写需要传递给 Python 程序的输入
# result = subprocess_run_program(path, user_input)
# print("Output of the program:")
# print(result)
