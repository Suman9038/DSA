# Naive solution: 0(n^3)
def longPre(s: str,n: int):
    for leng in range(n-1, 0, -1):
        flag = True
        for i in range(leng):
            if(s[i]!= s[n-leng+i]):
                flag = False
        if flag == True:
            return leng
    return 0

def fillLps(txt: str, lps: list[int]):
    for i in range(len(txt)):
        lps[i] = longPre(txt, i + 1)
        
txt = "abacab"
lps = [0] * len(txt)
fillLps(txt, lps)
print(lps)  # Output: [0, 0, 1, 0, 1, 2]

# Effecient Solution in O(n)
def filLps(s: str, lps: list[int]):
    n = len(s)
    leng = 0
    lps[0] = 0
    
    i = 1
    while(i<n):
        if(s[i]==s[leng]):
            leng+=1
            lps[i]= leng
            i+=1
        else :
            if leng == 0:
                lps[i] = 0
            else:
                leng= lps[leng-1]
                
txt = "abacab"
lps = [0] * len(txt)
filLps(txt, lps)
print(lps)  # Output: [0, 0, 1, 0, 1, 2]