from typing import List


def gcd(test_cases: List[str]) -> str :
    test_cases = [int(x) for x in test_cases]
    if test_cases[1] == 0 :
        return test_cases[0]
    else :
        return gcd([test_cases[0],test_cases[0]%test_cases[1]])