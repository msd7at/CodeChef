#link:-https://www.codechef.com/JUNE20B/problems/XYSTR

t=int(input())
for q in range(t):
    s=input()
    l=len(s)
    if l==1:
        print(0)
    else:
        c=0
        i=0
        while i<l-1:
            if (s[i]=="x" and s[i+1]=="y" ) or (s[i]=="y" and s[i+1]=="x" ):
                c+=1
                i=i+2
            else:
                i+=1
        print(c)
