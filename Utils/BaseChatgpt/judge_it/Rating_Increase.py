from typing import List


# 检查input是否符合IT
def judge_it_rating_increase(input: List[str]) -> bool:
    if len(input) == 0:
        return False
    # 尝试将第一行转换为整数，并检查其是否在1到10000之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10000:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t:
        return False
    # 检查每个测试用例
    for testcase in input[1:]:
        # 检查长度
        if not 2 <= len(testcase) <= 8:
            return False
        # 检查是否只包含数字
        if not testcase.isdigit():
            return False
        # 检查是否不以零开头
        if testcase[0] == '0':
            return False
    # 如果所有检查都通过，则返回True
    return True