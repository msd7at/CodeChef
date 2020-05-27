t=int(input())
for q in range(t):
    l,r=map(int,input().split())
    c=0
    for i in range(l,r+1):
        if i%10 in {2,3,9}:
            c+=1
    print(c)
        
