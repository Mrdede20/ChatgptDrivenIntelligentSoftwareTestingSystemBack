import os
import shutil


def copy_files(source_dir, target_dir, target_file_name, extensions=('.py', '.txt')):
    """
    Copies files with specified extensions from the source directory to the target directory.

    Args:
    source_dir (str): The path to the source directory where the files are located.
    target_dir (str): The path to the target directory where the files will be copied.
    extensions (tuple): A tuple of file extensions to include. Defaults to ('.py', '.txt').
    """
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Walk through the directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file ends with a desired extension
            if file.endswith(extensions):
                file_name_without_extension, file_extension = os.path.splitext(file)
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(target_dir+f"/{file_name_without_extension}", target_file_name)

                # Copy the file to the target directory
                shutil.copy(source_file_path, target_file_path)
                print(f"Copied {source_file_path} to {target_file_path}")


# 使用示例
# source_directory = '../../ProgramTobeTested/python_2024_04_21_11_40_01/buggy'
# target_file_name = 'PUT_code.py'
# source_directory = '../../ProgramTobeTested/python_2024_04_21_11_40_01/intention'
# target_file_name = 'intention.txt'
# target_directory = './data/python_2024_04_21_11_40_01'
#
# copy_files(source_directory, target_directory ,target_file_name)
