# 执行接口Pynguin
import os
import shutil

from Utils.Pynguin.copy_file import copy_all_files
from Utils.Pynguin.run_pynguin import run_all_pynguin


# 创建新文件
def create_new_file(file_path):
    # 确保目录存在
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 尝试创建文件，如果文件已存在，则抛出异常
    try:
        with open(file_path, 'x') as fp:
            pass  # 只创建文件，不写入数据
        print(f"File '{file_path}' created successfully.")
    except FileExistsError:
        print(f"File '{file_path}' already exists.")


def exec_pynguin(current_time):
    # 创建储存数据目录
    data_dir = f'./Utils/Pynguin/data/{current_time}'
    os.makedirs(os.path.dirname(data_dir), exist_ok=True)
    # 1、遍历源代码目录执行Pynguin
    run_all_pynguin(current_time)

    # 2、复制一些额外文件到目标目录
    test_code_dir = f'./ProgramTobeTested/{current_time}/test'
    os.makedirs(os.path.dirname(test_code_dir), exist_ok=True)
    shutil.move(f"./Utils/Pynguin/data/{current_time}",test_code_dir)

    # 3、移动Pynguin完成后的pynguin-report路径
    os.makedirs(os.path.dirname(data_dir), exist_ok=True)
    src_report_dir = f"./pynguin-report"
    dst_report_dir = f"./Utils/Pynguin/data/{current_time}/pynguin-report"
    shutil.move(src_report_dir, dst_report_dir)

    return "Pynguin"


# current_time = "python_2024_04_20_10_58_41"
# exec_pynguin(current_time)



