# Effecient Solution: 0(n):
def fact(n):
    fact = 1
    if n== 0 or n==1:
        return 1
    else:
        for i in range(2,n+1):
            fact = fact * i
    return fact
    
def lexRank(s: str):
    n = len(s)
    res = 1
    mul = fact(n)
    count = [0]*256
    for i in range(0,n):
        count[ord(s[i])]+=1
    for i in range(1,256):
        count[i]+= count[i-1]
    for i in range(n):
        mul //= (n - i)   
        res += count[ord(s[i]) - 1] * mul
        for j in range(ord(s[i]), 256):
            count[j]-=1
    return res

print(fact(5))
print(lexRank("STRING")) 
