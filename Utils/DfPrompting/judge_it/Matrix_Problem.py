from typing import List


def judge_it_matrix_problem(input: List[str]) -> bool:
    if len(input) == 0:
        return False
    # 解析第一行的n和m
    try:
        n, m = map(int, input[0].split())
        if not (2 <= n <= 50) or not (2 <= m <= 50):
            return False
    except ValueError:
        return False  # 如果转换失败或者不在范围内，返回False
    if len(input) != 1 + n + 2:
        return False
    # 检查后续的n行，每行应该有m个0或1的整数
    for i in range(1, n + 1):
        try:
            row = list(map(int, input[i].split()))
            if len(row) != m or any(a_ij < 0 or a_ij > 1 for a_ij in row):
                return False
        except ValueError:
            return False  # 如果转换失败或者不符合条件，返回False

    # 检查包含n个整数的下一行
    try:
        a_values = list(map(int, input[n + 1].split()))
        if len(a_values) != n or any(A_i < 0 or A_i > m for A_i in a_values):
            return False
    except ValueError:
        return False  # 如果转换失败或者不符合条件，返回False

    # 检查包含m个整数的下一行
    try:
        b_values = list(map(int, input[n + 2].split()))
        if len(b_values) != m or any(B_i < 0 or B_i > n for B_i in b_values):
            return False
    except ValueError:
        return False  # 如果转换失败或者不符合条件，返回False

    # 如果所有检查都通过，则返回True
    return True