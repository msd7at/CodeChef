t=int(input())
for i in range(t):
    n=int(input())
    a=[int(q) for q in input().split()]
    b=[int(q) for q in input().split()]
    so=0
    for p in range(n):
        xo=(a[p]*20)-(b[p]*10)
        if so > xo:
            xo=so
        
        so=xo
    if xo < 0:
        print(0)
    else:
        print(xo)
