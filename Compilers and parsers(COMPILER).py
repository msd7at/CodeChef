t=int(input())
for q in range(t):
    n=input()
    x=0
    ans=0
    c=0
    for i in n:
        if i=="<":
            x+=1
        else:
            x-=1
            if x<0:
                break
            if x==0:
                ans=c+1
        c+=1
    print(ans)
    
    
