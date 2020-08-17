t=int(input())
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
for q in range(t):
    n,a,b,k=map(int,input().split())
    ca=n//a
    caa=n//b
    g=gcd(a,b)
    lc=(a*b)//g
    s=n//lc
    ans=ca+caa-(2*s)
    if ans >=k:
        print('Win')
    else:
        print('Lose')
