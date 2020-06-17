#link:-https://www.codechef.com/JUNE20B/problems/PRICECON
#solution
t=int(input())
for q in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    r=0
    for i in l:
        s+=i
        if i>k:
            r+=k 
        else:
            r+=i
    print(s-r)
