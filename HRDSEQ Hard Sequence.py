t=int(input())
l=[0]
s={}
for i in range(1,128):
    if l[i-1] not in s:
        s[l[i-1]]=i
        l.append(0)
    else:
        l.append(i-s[l[i-1]])
        s[l[i-1]]=i
for q in range(t):
    n=int(input())
    
    print(l[:n].count(l[n-1]))
