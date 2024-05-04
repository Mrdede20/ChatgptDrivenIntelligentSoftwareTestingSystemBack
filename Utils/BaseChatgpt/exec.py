# 执行接口BaseChatgpt
import os
from Utils.BaseChatgpt.analyzeResults import analyzeResults
from Utils.BaseChatgpt.exportExcelFile import export_excel_file
from Utils.BaseChatgpt.extract_input_and_expectedOutput import extract_input_and_expectedOutput
from Utils.BaseChatgpt.generateTestCode import generateTestCode
from Utils.BaseChatgpt.myGeMini import myGeMini
from Utils.BaseChatgpt.convert_python_to_json import convert_python_to_json
from Utils.BaseChatgpt.copy_file import copy_file , copy_all_files


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


def exec_basechatgpt(current_time):
    # 创建储存数据目录
    data_dir = f'./Utils/BaseChatgpt/data/{current_time}'
    os.makedirs(os.path.dirname(data_dir), exist_ok=True)
    # 1、将指定目录下的buggy python文件转化为json文件
    buggy_source_dir = "./ProgramTobeTested/" + current_time + "/buggy"
    buggy_source_json_file = f'./Utils/BaseChatgpt/data/{current_time}/buggyProgram.json'
    create_new_file(buggy_source_json_file)
    convert_python_to_json(buggy_source_dir, buggy_source_json_file)

    # 2、提问大模型获取测试用例
    # 提问大模型所需program文件
    buggy_source_json_file = buggy_source_json_file
    # 保存大模型回复数据文件
    gemini_pro_reply_file = f'./Utils/BaseChatgpt/data/{current_time}/GeMiniProReply.json'
    create_new_file(gemini_pro_reply_file)
    # 每个程序生成测试用例的次数
    loop_num = 10
    myGeMini(buggy_source_json_file, gemini_pro_reply_file, loop_num)

    # 3、提取出大模型回复中的input和expectedOutput
    # 保存大模型回复数据的JSON文件路径
    gemini_pro_reply_file = gemini_pro_reply_file
    # 输出文件路径
    in_and_out_file = f'./Utils/BaseChatgpt/data/{current_time}/InAndOut.json'
    create_new_file(in_and_out_file)
    extract_input_and_expectedOutput(gemini_pro_reply_file, in_and_out_file)

    # 4、判断测试用例类型
    in_and_out_file = in_and_out_file
    analyze_results_file = f'./Utils/BaseChatgpt/data/{current_time}/TestcaseType.json'
    create_new_file(analyze_results_file)
    analyzeResults(in_and_out_file, analyze_results_file, current_time)

    # 5、生成测试代码
    # 创建储存测试代码目录
    test_code_dir = f'./ProgramTobeTested/{current_time}/test'
    os.makedirs(os.path.dirname(test_code_dir), exist_ok=True)
    in_and_out_file = in_and_out_file
    generateTestCode(in_and_out_file,test_code_dir,current_time)

    # 6、复制一些额外工具到目标目录
    extra_util_dir = './Utils/BaseChatgpt'
    test_code_extra_util_dir = f'./ProgramTobeTested/{current_time}/utils'
    os.makedirs(os.path.dirname(test_code_extra_util_dir), exist_ok=True)
    copy_file(extra_util_dir, test_code_extra_util_dir,"has_def_function.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "subprocess_run_program.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "judgeTestcaseType.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "dynamic_import_module.py")
    copy_file(extra_util_dir, test_code_extra_util_dir, "judgeTestcaseType_testcode.py")

    test_code_judge_it_dir = f'./ProgramTobeTested/{current_time}/judge_it'
    os.makedirs(os.path.dirname(test_code_judge_it_dir), exist_ok=True)
    copy_all_files("./Utils/BaseChatgpt/judge_it",test_code_judge_it_dir)

    # 7、导出excel文件
    test_case_type_file = f'./Utils/BaseChatgpt/data/{current_time}/TestcaseType.json'
    excel_file = f'./Utils/BaseChatgpt/data/{current_time}/analyzeResults.xlsx'
    export_excel_file(test_case_type_file, excel_file)

    return "BaseChatgpt"

