def filLps(s: str, lps: list[int]):
    n = len(s)
    leng = 0
    lps[0] = 0
    i = 1
    while i < n:
        if s[i] == s[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng == 0:
                lps[i] = 0
                i += 1 
            else:
                leng = lps[leng - 1]


def KMP(txt: str, pat: str):
    n = len(txt)
    m = len(pat)
    lps = [0] * m
    filLps(pat, lps)
    i, j = 0, 0
    while i < n:
        if pat[j] == txt[i]:  
            i += 1
            j += 1
        if j == m:
            print(i - j)
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]


# Example run
txt = "ababcababaad"
pat = "ababa"
KMP(txt, pat)  
