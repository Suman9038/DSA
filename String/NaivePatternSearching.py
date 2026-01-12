# Naive Solution : O((n-m+1)*m)

def pat(s: str, pat: str):
    n = len(s)
    m = len(pat)
    for i in range(0, n-m+1):
        j: int
        for j in range(0,m):
            if(pat[j]!= s[i+j]):
                break
        else:
            print(i)
            
            
pat("ABCABCD","ABCD")