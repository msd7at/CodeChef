t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=[0]*10
    for i in l:
        a[i-1]+=1
    #print(a)

    s={}
    m=10000000000
    for i in a:
        if i!=0:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
    ke=[]
    for bhj in s.values():
        ke.append(bhj)
    
    mak=max(ke)
    if ke.count(mak)>1:
        ans=[]
        for i in s:
            if s[i]==mak:
                ans.append(i)    
        print(min(ans))
    else:
        for i in s:
            if s[i]==mak:
                print(i)
                break
