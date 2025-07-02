# Naive solution  : theta(n) time , theta(n) aux space
def palinStr(str) :
    revStr= str[::-1] 
    # print(revStr)
    if str == revStr :
        print("It is palindrome")
    else :
        print("It is not palindrome")
    
# palinStr("ABBA")

# Efficient Solution : 0(n) , 0(1) aux space

def palinStrOptimized(str) :
    begin= 0
    end= len(str)-1
    
    while(begin<end) :
        if(str[begin]!=str[end]) :
            return False
        begin+=1
        end-=1
    
    return True
print(palinStrOptimized("ABBA"))

           