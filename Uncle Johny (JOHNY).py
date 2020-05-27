t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    k=int(input())
    c=0
    a=l[k-1]
    for i in l:
        if i <a:
            c +=1
    print(c+1)
