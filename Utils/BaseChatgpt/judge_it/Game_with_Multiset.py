from typing import List


def judge_it_game_with_multiset(input: List[str]) -> bool:
    if len(input) == 0:
        return False
    # 尝试将第一行转换为整数，并检查其是否在1到10^5之间
    try:
        m = int(input[0])
        if not 1 <= m <= 10 ** 5:
            return False
    except ValueError:
        return False  # 如果转换失败或不在范围内，返回False
    if len(input) != 1 + m:
        return False
    # 检查每一行查询是否符合要求
    for line in input[1:]:
        try:
            t_i, v_i = map(int, line.split())
            # 如果 t_i = 1，则检查 0 ≤ v_i <= 29
            if t_i == 1 and not (0 <= v_i <= 29):
                return False
            # 如果 t_i = 2，则检查 0 ≤ v_i ≤ 10^9
            if t_i == 2 and not (0 <= v_i <= 10 ** 9):
                return False
            # 如果 t_i 不是 1 或 2，则返回False
            if t_i not in [1, 2]:
                return False
        except ValueError:
            return False  # 如果转换失败或者行中没有两个整数，返回False

    # 如果所有检查都通过，则返回True
    return True