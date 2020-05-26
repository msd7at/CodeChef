t=int(input())
for i in range(t):
    s=input()
    v=0
    for j in s:
        if ord(j)>=48 and ord(j)<58:
            v+= int(j)
    print(v)
