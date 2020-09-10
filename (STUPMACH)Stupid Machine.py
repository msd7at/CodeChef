t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    mi=10000000000000
    for i in l:
        mi=min(i,mi)
        s=s+mi
    print(s)
