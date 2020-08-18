t=int(input())
for q in range(t):
    n=int(input())
    ans=10000000000000000
    ptr=False
    i=1
    while i**2 <=n:
        if n%i==0:
            x=(n//i-i)//2
            y=(n//i+i)//2
            if (x**2)+n==y**2 and x!=0:
                ans=min(ans,x)
                ptr=True
        i+=1
    if ans==0:
        print(-1)
    elif ptr:
        print(ans**2)
    else:
        print(-1)
