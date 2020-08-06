t=int(input())
for q in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    for i in l:
        if i%k==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
                        
