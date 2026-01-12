# Naive solution : O(nlogn) time 
 
def areAnagram(s1: str, s2:str) :
    if(len(s1) != len(s2)) :
        return False
    # print(sorted(s1))
    # print(sorted(s2))
    sort_s1 = sorted(s1)
    sort_s2 = sorted(s2)
    if(sort_s1 == sort_s2) :
        return True

# print(areAnagram("listen", "silent"))


# Effecient Solution : 0() :
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
print(areAnagramOptimised("listen", "silent"))