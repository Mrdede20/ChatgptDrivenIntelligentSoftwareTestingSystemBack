import os
from pathlib import Path


# 遍历指定目录下全部的py文件，提取出它的文件名（把.py也去掉），然后在另外一个指定目录下新建一个子目录，子目录名字按文件名命名
def create_subdirs_for_py_files(source_dir, target_dir):
    # 确保源目录和目标目录是Path对象
    source_dir = Path(source_dir)
    target_dir = Path(target_dir)

    # 遍历源目录中的所有文件
    for file_path in source_dir.glob('*.py'):
        # 获取不带.py的文件名
        file_name = file_path.stem

        # 创建目标子目录路径
        new_dir_path = target_dir / file_name

        # 如果目标子目录不存在，则创建它
        if not new_dir_path.exists():
            new_dir_path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {new_dir_path}")
        else:
            print(f"Directory already exists: {new_dir_path}")


# 使用示例
# source_directory = '../../ProgramTobeTested/python_2024_04_21_11_40_01/buggy'
# target_directory = './data/python_2024_04_21_11_40_01'
# create_subdirs_for_py_files(source_directory, target_directory)
