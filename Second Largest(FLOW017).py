t=int(input())
for q in range(t):
    a,b,c=map(int,input().split())
    m=max(a,b,c)
    if a==m:
        if b==max(b,c):
            print(b)
        else:
            print(c)
    elif b==m:
        if a==max(a,c):
            print(a)
        else:
            print(c)
    else:
        if a==max(a,b):
            print(a)
        else:
            print(b)
