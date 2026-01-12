def checkRotation(s1: str, s2: str):
    if(len(s1) != len(s2)):
        return False
    s3 = s1+s2
    return(s3.find(s2)>=0)

print(checkRotation("ABCD", "CDAB"))