N=200
l=[False]*(N+1)
l[0]=True
l[1]=True
k=0
for i in range(2,N//2):
    for j in range(i**2,N+1,i):
        l[j]=True
x=[]
for i in range(N+1):
    if not l[i]:
        x.append(i)
t=int(input())
for q in range(t):
    n=int(input())
    s=set()
    for i in range(len(x)):
        if x[i]>=n:
            break
        for j in range(i+1,len(x)):
            if x[j]>=n:
                break
            if x[i]*x[j] <=n:
                s.add(x[i]*x[j])
    d=0
    for i in s:
        if n-i in s:
            print('YES')
            d=1
            break
    if d==0:
        print('NO')
