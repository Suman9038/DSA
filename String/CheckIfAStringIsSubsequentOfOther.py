# Effecient Solution : O(n+m)

def isSubse(str1, str2) :
    j=0
    i=0
    while(i<len(str1) and j< len(str2)) :
        if(str1[i] == str2[j]) :
            i+=1
        j+=1
        
    if(len(str1)==i) :
        return True
    else :
        return False
    
    
print(isSubse("abc", "aebdc"))
            
            
