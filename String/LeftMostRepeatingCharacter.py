# Naive Solution: O(n^2): 
def isLeft(s: str) :
    for i in range(0,len(s)) :
        for j in range(i+1,len(s)) :
            if s[i] == s[j] :
                return i
    return -1

print(isLeft("abccbd"))

# Effecient approach(1) with two loops :
def left(s: str): 
    count =[0]*256
    for i in range(0, len(s)):
        count[ord(s[i])]+=1
    for i in count :
        if count[ord(s[i])] > 1:
            return i
    return -1

print(left("abccbd"))

# Approach (2) with single loop 
def isLeftOptimized(s: str) :
    visited = [False]*256
    res = -1
    for i in range(len(s)-1,-1,-1) :
        if visited[ord(s[i])] :
            res = i
        else :
            visited[ord(s[i])]= True
    return res

print(isLeftOptimized("abccbd"))