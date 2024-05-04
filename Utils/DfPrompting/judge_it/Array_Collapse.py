from typing import List


def judge_it_array_collapse(input: List[str]) -> bool:
    if len(input) == 0:
        return False
    # 尝试将第一行转换为整数，并检查其是否在1到10^4之间
    try:
        t = int(input[0])
        if not 1 <= t <= 10 ** 4:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + t * 2:
        return False
    # 初始化n的总和计数器
    total_n = 0

    # 索引从1开始，因为第0个元素是t
    index = 1
    for _ in range(t):
        # 检查是否有足够的行
        if index >= len(input):
            return False

        # 尝试将当前行转换为整数n，并检查其是否在1到3 * 10^5之间
        try:
            n = int(input[index])
            if not 1 <= n <= 3 * 10 ** 5:
                return False
        except ValueError:
            return False  # 如果转换失败或不在范围内，返回False

        # 增加n的总和
        total_n += n

        # 检查n的总和是否超过了3 * 10^5
        if total_n > 3 * 10 ** 5:
            return False

        # 移动到包含n个整数的行
        index += 1

        # 检查是否有足够的行
        if index >= len(input):
            return False

        # 获取该行的整数，并检查它们是否互不相同
        integers = input[index].split()
        if len(integers) != n:
            return False  # 如果整数的数量不等于n，返回False

        # 尝试将整数转换为int，并检查范围
        try:
            integer_values = [int(value) for value in integers]
            if not all(1 <= value <= 10 ** 9 for value in integer_values):
                return False
            if len(set(integer_values)) != n:
                return False  # 如果整数不是互不相同的，返回False
        except ValueError:
            return False  # 如果转换失败，返回False

        # 移动到下一个测试用例的第一行
        index += 1

    # 如果所有检查都通过，则返回True
    return True
