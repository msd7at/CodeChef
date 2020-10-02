t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    g=12
    for i in range(n)   :
        if ( ( ((i+1)%l[i] !=0))) :
            print("NO")
            g=22
            break
    if g==12:
        print("YES")
