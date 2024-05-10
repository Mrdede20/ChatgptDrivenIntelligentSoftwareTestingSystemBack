
def lcs_length(s: str, t: str) -> int:
    max_len = 0
    for i in range(len(s)):
        for j in range(len(t)):
            k = 0
            while i + k < len(s) and j + k < len(t) and s[i+k] == t[j+k]:
                k += 1
            if k > max_len:
                max_len = k
    return max_len
