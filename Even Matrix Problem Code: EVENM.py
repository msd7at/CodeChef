#link:-https://www.codechef.com/JUNE20B/problems/EVENM/
t=int(input())
for q in range(t):
    n=int(input())
    c=1
    ar=[]
    for i in range(n):
        d=[]
        for j in range(n):
            d.append(c)
            c+=1
        if i%2==1:
            d=d[::-1]
        ar.append(d)
    for i in range(n):
        print(*ar[i])
                
            
        
    
            
