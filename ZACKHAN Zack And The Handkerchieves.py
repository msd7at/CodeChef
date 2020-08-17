t=int(input())
def hcf(a,b):
    if b==0:
        return a
    return hcf(b,a%b)
    
for i in range(t):
    m,n=map(int,input().split())
    j=hcf(m,n)
    print(j)
