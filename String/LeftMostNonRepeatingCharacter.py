# Nainve Solution : O(n^2) :
def nonRep(s: str) :
    for i in range(0, len(s)) :
        flag = False
        for j in range(0, len(s)) :
            if(i!=j and s[i]== s[j]) :
                flag = True
                break
        if(flag == False): 
            return i
    return -1

print(nonRep("abcabc"))

#Effecient Solution with two loop
def left(s: str): 
    count =[0]*256
    for i in range(0, len(s)):
        count[ord(s[i])]+=1
    for i in count :
        if count[ord(s[i])] == 1:
            return i
    return -1

print(left("abcd"))

# Approach (2) with single loop
def nonR(s:str) :
    fi = [-1]*256
    for i in range(0,len(s)) :
        if(fi[ord(s[i])] == -1) :
            fi[ord(s[i])] = i
        else :
            fi[ord(s[i])] = -2 # For visited element
    res = 2**31 - 1
    for i in range(256) :
        if (fi[i]>=0):
            res= min(res,fi[i]) 
    return -1 if res == 2**31 - 1 else res
        
print(nonR("abcd"))
