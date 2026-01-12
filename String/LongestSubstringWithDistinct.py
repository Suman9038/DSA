# Naive Solution :0(n^3):

def areDistinct(s: str, i: int, j: int):
    visited = [False]*256
    
    for k in range(i,j+1):
        if visited[ord(s[k])]:
            return False
        visited[ord(s[k])]= True
    return True

def longDistinct(s:str):
    n= len(s)
    res = 0
    for i in range(n):
        for j in range(n):
            if(areDistinct(s,i,j)):
                res = max(res,j-i+1)
    return res
# print(longDistinct("aaa"))

# Betters Solution: 0(n^2):
def longestDist(s: str):
    n= len(s)
    res = 0
    for i in range(n):
        visited = [False]*256
        for j in range(i,n):
            if visited[ord(s[j])]:
                break
            else : 
                res = max(res, j-i+1)
                visited[ord(s[j])]= True
    return res
print(longestDist("aaa"))

#Effecient Solution: 0(n):

def longestDistinct(s: str):
    n = len(s)
    res = 0
    i=0
    prev = [-1] * 256
    for j in range(n):
        i = max(i, prev[ord(s[j])] + 1)   
        maxEnd = j - i + 1
        res = max(res, maxEnd)
        prev[ord(s[j])] = j  
    return res
print(longestDistinct("aaa"))   