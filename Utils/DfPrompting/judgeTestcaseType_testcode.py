from has_def_function import has_specific_function
from subprocess_run_program import subprocess_run_program
from judgeTestcaseType import judge_test_case_type
from dynamic_import_module import dynamic_import_module


def judgeTestcaseType_testcode(filename,input_data,replyStage1,expectedOutput):
    if type(input_data) is str:
        input_data = input_data.split("\n")
        expectedOutput = expectedOutput.split("\n")

    if replyStage1 == "no":
        testcaseType = "noBugs"
    else:
        expected_output = expectedOutput
        # 判断it
        judge_it_file_path = "../judge_it/" + filename
        judge_it_function_name = "judge_it_" + filename.lower()[:-3]  # 把大写字母改为小写字母、同时舍弃.py
        judge_it_arguments = [input_data]
        if not dynamic_import_module(judge_it_file_path, judge_it_function_name, *judge_it_arguments):
            testcaseType = "IT"
        else:
            # 获取buggy程序的输出
            buggy_file_path = "../" + "/buggy/" + filename  # Function
            buggy_function_name = filename.lower()[:-3]
            if has_specific_function(buggy_file_path, buggy_function_name):
                buggy_arguments = [input_data]
                buggy_output = str(dynamic_import_module(buggy_file_path, buggy_function_name, *buggy_arguments))
            else:
                # 使用换行符 '\n' 将 input_data 中的元素连接成一个字符串
                buggy_subprocess_input = "\n".join(input_data)
                buggy_output = subprocess_run_program(buggy_file_path, buggy_subprocess_input)
            # 获取correct程序的输出
            correct_file_path = "../" + "/correct/" + filename
            correct_function_name = filename.lower()[:-3]
            if has_specific_function(buggy_file_path, correct_function_name):
                correct_arguments = [input_data]
                correct_output = str(dynamic_import_module(correct_file_path, correct_function_name, *correct_arguments))
            else:
                # 使用换行符 '\n' 将 input_data 中的元素连接成一个字符串
                correct_subprocess_input = "\n".join(input_data)
                correct_output = subprocess_run_program(correct_file_path, correct_subprocess_input)
            # 判断被测程序有没有经过函数包装,决定是否重新调整expected_output数据格式
            if has_specific_function(buggy_file_path, buggy_function_name):
                testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output[0]+"\n" if len(expected_output) == 1 else "\n".join(expected_output))
            else:
                testcaseType = judge_test_case_type(buggy_output, correct_output, expected_output[0]+"\n" if len(expected_output) == 1 else "\n".join(expected_output))
    return testcaseType
