t=int(input())
for q in range(t):
    s=input()
    l=len(s)
    if l<2:
        print(0)
    elif l==2:
        print(1)
    else:
        se=set()
        for i in range(l-1):
            se.add(s[i]+s[i+1])
        print(len(se))
                
