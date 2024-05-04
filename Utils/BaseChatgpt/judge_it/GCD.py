from typing import List


def judge_it_gcd(input: List[str]) -> bool:
    # Check if both elements in the input list are integers
    if len(input) == 2 and all(isinstance(int(item), int) for item in input):
        return True
    else:
        return False

