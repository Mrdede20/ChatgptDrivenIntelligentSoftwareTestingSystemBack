from typing import List


def judge_it_swap_and_delete(input: List[str]) -> bool:
    if len(input) == 0:
        return False
    # 尝试将第一行转换为整数，并检查其是否在1到10000之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10 ** 4:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t:
        return False
    # 检查总长度是否不超过2 * 10^5
    total_length = sum(len(testcase) for testcase in input[1:])
    if total_length > 2 * 10 ** 5:
        return False

    # 检查每个测试用例
    for testcase in input[1:]:
        # 检查长度
        if not 1 <= len(testcase) <= 2 * 10 ** 5:
            return False
        # 检查是否为二进制字符串
        if not set(testcase).issubset({'0', '1'}):
            return False

    # 如果所有检查都通过，则返回True
    return True