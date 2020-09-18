t=int(input())
for i in range(t):
    d,n=map(int,input().split())
    s=0
    for i in range(d):
        s=(n*(n+1))//2
        n=s
    print(s)
    
    
