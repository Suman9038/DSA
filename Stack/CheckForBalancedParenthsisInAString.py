def matching(a,b):
    return(
        (a=="(" and b==")")
        or
        (a=="[" and b=="]")
        or
        (a=="{" and b=="}")
        
    )

def isBalanced(s: str):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            elif not matching(stack[-1], char):
                return False
            else:
                stack.pop()
    return not stack
    
print(isBalanced("{()}"))