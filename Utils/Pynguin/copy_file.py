import shutil
import os


def copy_file(source_path, target_path, file_name):
    """
    复制文件到指定目录。
    """
    full_source_path = os.path.join(source_path, file_name)
    full_target_path = os.path.join(target_path, file_name)
    os.makedirs(os.path.dirname(full_target_path), exist_ok=True)  # 确保目标目录存在
    shutil.copy(full_source_path, full_target_path)
    print(f"文件 {file_name} 已从 {source_path} 复制到 {target_path}")


def copy_all_files(source_directory, target_directory):
    """
    将指定源目录下的所有文件复制到目标目录下。
    """
    os.makedirs(target_directory, exist_ok=True)  # 确保目标目录存在
    for file_name in os.listdir(source_directory):
        full_file_name = os.path.join(source_directory, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, target_directory)
            print(f"已复制 {file_name} 到 {target_directory}")