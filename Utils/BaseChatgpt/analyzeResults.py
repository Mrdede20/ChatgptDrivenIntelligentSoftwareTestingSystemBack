import json

from Utils.BaseChatgpt.has_def_function import has_specific_function
from Utils.BaseChatgpt.subprocess_run_program import subprocess_run_program
from Utils.BaseChatgpt.judgeTestcaseType import judge_test_case_type
from Utils.BaseChatgpt.dynamic_import_module import dynamic_import_module


def analyzeResults(source_file ,target_file ,current_time):
    # 打开 JSON 文件并读取数据
    with open(source_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 遍历 JSON 数据中的每一项
    for item in data:
        # 提取 filename、input、replyStage1 和 expectedOutput
        filename = item.get('filename', '')
        input_data = item.get('input', [])
        replyStage1 = item.get('replyStage1', '')
        buggy_output = []
        correct_output = []
        if replyStage1 == "no":
            testcaseType = "noBugs"
            item['testcaseType'] = testcaseType
        else:
            expected_output = item.get('expectedOutput', [])
            # 判断it
            judge_it_file_path = "./Utils/BaseChatgpt/judge_it/"+filename
            judge_it_function_name = "judge_it_"+filename.lower()[:-3] # 把大写字母改为小写字母、同时舍弃.py
            judge_it_arguments = [input_data]
            if not dynamic_import_module(judge_it_file_path, judge_it_function_name, *judge_it_arguments):
                testcaseType = "IT"
            else:
                # 获取buggy程序的输出
                buggy_file_path = "./ProgramTobeTested/" + current_time + "/buggy/" +filename #Function
                buggy_function_name = filename.lower()[:-3]
                if has_specific_function(buggy_file_path,buggy_function_name):
                    buggy_arguments = [input_data]
                    buggy_output = str(dynamic_import_module(buggy_file_path, buggy_function_name, *buggy_arguments))
                else:
                    # 使用换行符 '\n' 将 input_data 中的元素连接成一个字符串
                    buggy_subprocess_input = "\n".join(input_data)
                    buggy_output = subprocess_run_program(buggy_file_path ,buggy_subprocess_input)
                # 获取correct程序的输出
                correct_file_path = "./ProgramTobeTested/" + current_time + "/correct/" +filename
                correct_function_name = filename.lower()[:-3]
                if has_specific_function(buggy_file_path ,correct_function_name):
                    correct_arguments = [input_data]
                    correct_output = str(dynamic_import_module(correct_file_path, correct_function_name, *correct_arguments))
                else:
                    # 使用换行符 '\n' 将 input_data 中的元素连接成一个字符串
                    correct_subprocess_input = "\n".join(input_data)
                    correct_output = subprocess_run_program(correct_file_path ,correct_subprocess_input)
                # 判断被测程序有没有经过函数包装,决定是否重新调整expected_output数据格式
                if has_specific_function(buggy_file_path, buggy_function_name):
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output[0]+"\n" if len(expected_output) == 1 else "\n".join(expected_output))
                else:
                    testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output[0]+"\n" if len(expected_output) == 1 else "\n".join(expected_output))

            item['testcaseType'] = testcaseType
        item['buggy_output'] = buggy_output
        item['correct_output'] = correct_output
    try:
        # 将修改后的数据写回JSON文件
        with open(target_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("分析测试用例类型结果已成功写入"+target_file)
    except FileNotFoundError:
        # 文件未找到时的异常处理
        print(f"错误：找不到文件或无法打开文件 '{target_file}'。")
    except IOError:
        # 文件读写错误的异常处理
        print(f"错误：写入文件 '{target_file}' 时发生错误。")
    except Exception as e:
        # 其他异常的处理
        print(f"发生未知错误：{e}")

# 调用函数并打印结果
# 用于判断测试用例类型源文件
# current_time = "python_2024_04_24_19_31_18"
# analyze_results_file = f'data/{current_time}/TestcaseType.json'
# in_and_out_file = f'data/{current_time}/InAndOut.json'
# analyzeResults(in_and_out_file, analyze_results_file, current_time)
