import json

# 创建新文件
import os

from Utils.DfPrompting.has_def_function import has_specific_function


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


def generateTestCode(in_and_out_file, test_code_dir, current_time):

    # 读取 JSON 文件
    with open(in_and_out_file, 'r') as file:
        test_cases = json.load(file)

    last_filename = ""
    file_handler = None

    for case in test_cases:
        filename = case['filename']
        iteration = case['iteration']
        input_data = case['input']
        expected_output = case['expectedOutput']
        reply_stage1 = case.get('replyStage1', '')

        # 检查是否需要创建新的测试文件
        if filename != last_filename:
            if file_handler:
                file_handler.close()
            test_filename = f"Test_{filename}"
            test_filepath = test_code_dir+ '/' +test_filename
            create_new_file(test_filepath)
            file_handler = open(test_filepath, 'w')

            # 写入导入语句
            imports = [
                "import unittest",
                "import sys",
                "import os",
                "project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))",
                "utils_dir = os.path.join(project_dir, 'utils')",
                "sys.path.append(utils_dir)",
                "from utils import judgeTestcaseType_testcode",
                "",
                ""
            ]
            file_handler.write('\n'.join(imports) + '\n')

            # 开始定义测试类
            class_definition = f"class {test_filename[:-3]}(unittest.TestCase):"
            file_handler.write(class_definition + '\n')

        # 测试方法定义
        test_method_name = f"def test_{filename.lower()[:-3]}_case_{iteration}(self):"
        file_handler.write('\t' + test_method_name + '\n')

        # 写入测试内容
        # 判断被测程序有没有经过函数包装
        buggy_file_path = "./ProgramTobeTested/" + current_time + "/buggy/" + filename  # Function
        buggy_function_name = filename.lower()[:-3]
        if has_specific_function(buggy_file_path, buggy_function_name):
            inputs_representation = f"\t\tinput = {repr(input_data)}"
            expected_output_representation = f"\t\texpectedOutput = {repr(expected_output)}"
        else:
            # 使用换行符 '\n' 将 input_data 中的元素连接成一个字符串
            input_data_temp = "\n".join(input_data)
            inputs_representation = f"\t\tinput = {repr(input_data_temp)}"
            expected_output_temp = "\n".join(expected_output)
            expected_output_representation = f"\t\texpectedOutput = {repr(expected_output_temp)}"

        testcase_type_line = f"\t\ttestcaseType = judgeTestcaseType_testcode.judgeTestcaseType_testcode('{filename}', input, '{reply_stage1}', expectedOutput)"

        file_handler.write(inputs_representation + '\n')
        file_handler.write(expected_output_representation + '\n')
        file_handler.write(testcase_type_line + '\n')

        # 写入断言语句
        assert_statement = f"\t\tself.assertEqual(\"FT-IA\" , testcaseType)"
        file_handler.write(assert_statement + '\n\n')

        last_filename = filename

    if file_handler:
        file_handler.close()

# 调用函数
# generateTestCode('data/python_2024_04_16_18_30_40/InAndOut.json', './test_dir')
