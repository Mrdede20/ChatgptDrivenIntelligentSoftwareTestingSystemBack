# 执行接口DfPrompting
import os

from Utils.DfPrompting.analyzeResults import analyzeResults
from Utils.DfPrompting.generateTestCode import generateTestCode
from Utils.DfPrompting.DP import run
from Utils.DfPrompting.append_to_json import append_to_json
from Utils.DfPrompting.check_file_exists import check_file_exists
from Utils.DfPrompting.copy_py_files import copy_files
from Utils.DfPrompting.create_subdirs_for_py_files import create_subdirs_for_py_files
from Utils.DfPrompting.copy_file import copy_file , copy_all_files
from Utils.DfPrompting.exportExcelFile import export_excel_file


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


def exec_dfprompting(current_time):
    # 创建储存数据目录
    data_dir = f'./Utils/DfPrompting/data/{current_time}'
    os.makedirs(os.path.dirname(data_dir), exist_ok=True)

    # 1、为每一个PUT新建一个储存数据的目录
    source_directory = f'./ProgramTobeTested/{current_time}/buggy'
    target_directory = f'./Utils/DfPrompting/data/{current_time}'
    create_subdirs_for_py_files(source_directory, target_directory)

    # 2、为每一个储存PUT数据的目录设置好intention和PUT_code
    target_directory = f'./Utils/DfPrompting/data/{current_time}'
    source_directory = f'./ProgramTobeTested/{current_time}/buggy'
    target_file_name = 'PUT_code.py'
    copy_files(source_directory, target_directory, target_file_name)
    source_directory = f'./ProgramTobeTested/{current_time}/intention'
    target_file_name = 'intention.txt'
    copy_files(source_directory, target_directory, target_file_name)

    # # 3、遍历指定目录下全部的子目录执行拆分提示
    parent_directory = f'./Utils/DfPrompting/data/{current_time}'
    in_and_out_file = f"./Utils/DfPrompting/data/{current_time}/InAndOut.json"
    for item in os.listdir(parent_directory):
        # Full path of the item
        item_path = os.path.join(parent_directory, item)
        # Check if the item is a directory
        if os.path.isdir(item_path):
            intention_provided = check_file_exists(f'./Utils/DfPrompting/data/{current_time}/{item}', 'intention.txt')
            run_result_count = 0  # 初始化变量
            while run_result_count != 10:
                # 执行拆分提示
                found, input_data, result_1_output = run(intention_provided, current_time, item)
                if found:
                    run_result_count += 1
                    df_item = {
                        "filename": item + ".py",
                        "iteration": run_result_count,
                        "input": input_data.split("\n"),
                        "expectedOutput": result_1_output.split("\n")
                    }
                    # 追加df_item字典到 JSON 文件
                    append_to_json(df_item, in_and_out_file)
    # 4、判断测试用例类型
    in_and_out_file = in_and_out_file
    analyze_results_file = f'./Utils/DfPrompting/data/{current_time}/TestcaseType.json'
    create_new_file(analyze_results_file)
    analyzeResults(in_and_out_file, analyze_results_file, current_time)

    # 5、生成测试代码
    # 创建储存测试代码目录
    test_code_dir = f'./ProgramTobeTested/{current_time}/test'
    os.makedirs(os.path.dirname(test_code_dir), exist_ok=True)
    in_and_out_file = in_and_out_file
    generateTestCode(in_and_out_file,test_code_dir,current_time)

    # 6、复制一些额外工具到目标目录
    extra_util_dir = './Utils/DfPrompting'
    test_code_extra_util_dir = f'./ProgramTobeTested/{current_time}/utils'
    os.makedirs(os.path.dirname(test_code_extra_util_dir), exist_ok=True)
    copy_file(extra_util_dir, test_code_extra_util_dir,"has_def_function.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "check_data_type.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "subprocess_run_program.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "judgeTestcaseType.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "dynamic_import_module.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "judgeTestcaseType_testcode.py")

    test_code_judge_it_dir = f'./ProgramTobeTested/{current_time}/judge_it'
    os.makedirs(os.path.dirname(test_code_judge_it_dir), exist_ok=True)
    copy_all_files("./Utils/DfPrompting/judge_it",test_code_judge_it_dir)

    # 7、导出excel文件
    test_case_type_file = f'./Utils/DfPrompting/data/{current_time}/TestcaseType.json'
    excel_file = f'./Utils/DfPrompting/data/{current_time}/results.xlsx'
    export_excel_file(test_case_type_file, excel_file)

    return "DfPrompting"


# current_time = "python_2024_04_21_11_40_01"
# exec_dfprompting(current_time)