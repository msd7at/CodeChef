t=int(input())
for e in range(t):
    n=int(input())
    s=input()
    ca,cb=n,n
    sa,sb=0,0
    for i in range(0,2*n):
        if i%2==0:
            sa=sa+(int(s[i]))
            ca-=1
        else:
            sb=sb+(int(s[i]))
            cb-=1
        if sa>sb+cb:
            print(i+1)
            break
        elif sb>sa+ca:
            print(i+1)
            break
        elif sa==sb and i==(2*n)-1:
            print(i+1)
            break
            
