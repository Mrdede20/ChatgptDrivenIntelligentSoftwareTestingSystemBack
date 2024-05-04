import importlib.util


# 这个用来运行经过函数包装的程序
def dynamic_import_module(file_path, function_name, *args):
    # 通过文件路径加载模块
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # 获取要执行的函数
    target_function = getattr(module, function_name)

    # 检查传递的参数数量是否与函数期望的参数数量匹配
    expected_arg_count = target_function.__code__.co_argcount
    if len(args) != expected_arg_count:
        return f"Error: Function {function_name} expects {expected_arg_count} arguments, but {len(args)} were provided"

    # 执行函数并返回结果
    return target_function(*args)


# # 示例用法
# file_path = "./judge_it/Array_Collapse.py"
# function_name = "judge_it_array_collapse"
# arguments = [["1", "5", "1 2 3 4 5"]]
# result = dynamic_import_module(file_path, function_name, *arguments)
# print(result)
