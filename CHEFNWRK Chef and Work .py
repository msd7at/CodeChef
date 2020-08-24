t=int(input())
import collections 
for q in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    i=n-1
    ans=0
    x=0
    while i>=0 :
        if l[i]>k:
            print(-1)
            x=1
            break
        else:
            tem=0
            while i>=0 and tem+l[i]<=k:
                tem+=l[i]
                i-=1
            ans+=1
    if x==0:
        print(ans)
