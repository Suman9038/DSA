# Effecient Solution:

def reversed_word(char: list, low: int, high: int):
    while(low<high):
        char[low], char[high] = char[high], char[low]
        low+=1
        high-=1

def revString(s: str) :
    char = list(s)
    start = 0
    for end in range(0,len(char)):
        if(s[end]==" "):
            reversed_word(char,start,end-1)
            start= end +1
    reversed_word(char,start,len(s)-1)
    reversed_word(char,0,len(s)-1)
    return ''.join(char) 


print(revString("i love python"))