# Naive Solution: 0((n-m+1)*m)
def areAnagramOptimised(s1: str, s2: str):
    if(len(s1) != len(s2)) :
        return False
    count=[0]*256
    for i in range(0,len(s1)) :
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
        
    for c in count :
        if c != 0 :
            return False
    return True

def isPresent(txt: str, pat: str):
    n = len(txt)
    m = len(pat)
    
    for i in range(n-m+1):
        if(areAnagramOptimised(pat, txt[i:i+m])):
            return True
    return False

print(isPresent("geeksforgeeks","frog"))


# Effecient Solution 0(n*char)Time, Aux:0(char)

def areSame(CT, CP):
    for i in range(256):
        if CT[i] != CP[i]:
            return False
    return True

def isPresentOptimised(txt: str, pat: str):
    CT = [0]*256
    CP = [0]*256
    
    for i in range(len(pat)):
        CT[ord(txt[i])]+=1
        CP[ord(pat[i])]+=1
        
    for i in range(len(pat), len(txt)):
        if(areSame(CT,CP)):
            return True
        CT[ord(txt[i])]+=1
        CT[ord(txt[i-len(pat)])]-=1
    
    return areSame(CT, CP)

print(isPresentOptimised("geeksforgeeks", "frog"))  # True
print(isPresentOptimised("geeksforgeeks", "seek"))  # False
