def rbAlgo(txt: str, pat: str):
    m= len(pat)
    n= len(txt)
    q= 33
    h= 1
    d=5
    for i in range( m-1):
        h = (h*d)%q
    
    p = 0
    t = 0
    for i in range(m):
        p = (p*d+ ord(pat[i]))%q
        t = (t*d+ ord(txt[i]))%q
    
    for i in range(n-m+1):
        if p == t:
            flag = True
            for j in range(0,m):
                if(txt[i+j]!=pat[j]):
                    flag = False
                    break
            if(flag == True):
                print(i)
                
        if(i<n-m):
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if(t<0):
                t= t+q
                
                
rbAlgo("ABCABCD","ABCD")