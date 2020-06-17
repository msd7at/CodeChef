#link:-https://www.codechef.com/JUNE20B/problems/GUESSG
#NOTE;_ THIS SOLUTION IS FOR 15 POINTS
n=int(input())
pol=1
pel=1
peh=n
poh=n
o=(pol+poh)
if o%2==0:
    o=o//2
    o=o+1
else:
    o=o//2
e=o
c=1
while True:
    if c%2==1:
        print(o)
        a=input()
        if a=="L":
            poh=o
            if (pol+poh)%2==0:
                o=(pol+o)//2
                o=o+1
            else:
                o=((pol+poh)//2)
        elif a=="G":
            pol=o
            if (pol+poh) %2==0:
                o=(poh+pol)//2
                o+=1
            else:
                o=(pol+poh)//2
        else:
            break
    else:
        print(e)
        a=input()
        if a=="L":
            peh=e
            if (pel+peh)%2==0:
                e=(pel+e)//2
                e=e+1
            else:
                e=((pel+peh)//2)
        elif a=="G":
            pel=e
            if (pel+peh) %2==0:
                e=(peh+pel)//2
                e=e+1
            else:
                e=(pel+peh)//2
        else:
            break
    c+=1
       
