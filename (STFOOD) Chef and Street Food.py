t=int(input())
for e in range(t):
    n=int(input())
    ma=-10
    for e in range(n):
        s,p,v=map(int,input().split())
        m=(p//(s+1))*v
        ma=max(m,ma)
    print(ma)
