#LINK:-https://www.codechef.com/JUNE20B/problems/COVDSMPL
#note THIS SOLUTION IS FOR .88 POINTS
t=int(input())
for q in range(t):
    n,p=map(int,input().split())
    a=[]
    z=0
    
    for i in range(n):
        d=[]
        for j in range(n):
            d.append(0)
        a.append(d)
    while z<n:
        print(1,z+1,1,z+1,n)
        x=int(input())
        if x==0:
            ass=z+1
        else:
            break
        z+=1
    nss=n
    for i in range(n-1,-1,-1):
        print(1,i+1,1,i+1,n)
        x=int(input())
        if x==0:
            nss=i 
        else:
            break
    lss=0
    for i in range(n):
        print(1,1,i+1,n,i+1)
        x=int(input())
        if x==0:
            lss=lss+1
        else:
            break
    rss=n
    for i in range(n-1,-1,-1):
        print(1,1,i+1,n,i+1)
        x=int(input())
        if x==0:
            rss=i 
        else:
            break
        
    for r1 in range(z,nss):
        print(1,r1+1,1,r1+1,n)
        x=int(input())
        if x==0:
            u="f"
        else:
            for c1 in range(lss,rss):
                print(1,r1+1,c1+1,r1+1,c1+1)
                x=int(input())
                if x==1:
                    a[r1][c1]=1
                if x==-1:
                    break
    print(2)
    for i in range(n):
        print(*a[i])
    x=int(input())
    if x==-1:
        break
