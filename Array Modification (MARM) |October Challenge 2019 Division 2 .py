t=int(input())
for o in range(t):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    if n<k:
        if n%2==0:
            t=n*3
            op=k%t
            for i in range(op):
                a=A[i%n]
                b=A[n-(i%n)-1]
                A[i%n]=a^b
        else:
            h=int((n-1)/2)
            t=(n*3)
            op=k%t
            if op <=h:
                op=op+t
            for i in range(op):
                a=A[i%n]
                b=A[n-(i%n)-1]
                A[i%n]=a^b
    else:
        for i in range(k):
            a=A[i%n]
            b=A[n-(i%n)-1]
            A[i%n]=a^b
    print(*A)
