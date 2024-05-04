# 检查是否符合FT-IA、FT-Ia、FT-ia、IncorrectPT、CorrectPT
def judge_test_case_type(buggy_output, correct_output, expected_output):
    if buggy_output != expected_output and expected_output == correct_output and buggy_output != correct_output:
        return "FT-IA"
    if buggy_output != expected_output and expected_output != correct_output and buggy_output != correct_output:
        return "FT-Ia"
    if buggy_output != expected_output and expected_output != correct_output and buggy_output == correct_output:
        return "FT-ia"
    if buggy_output == expected_output:
        if buggy_output != correct_output:
            return "IncorrectPT"
        elif buggy_output == correct_output:
            return "CorrectPT"

