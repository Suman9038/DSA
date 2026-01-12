# Improved Naive : theta(n)

def improvedPattern(s: str, pat: str):
    n = len(s)
    m = len(pat)
    i=0
    while i <= n-m+1:
        j = 0
        while j < m and (pat[j] == s[i+j]):
            j += 1
        if j == m :
            print(i)
        if j == 0:
            i+=1
        else :
            i= (i+j)
            
improvedPattern("ABCABCD","ABCD")