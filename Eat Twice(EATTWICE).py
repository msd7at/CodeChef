# solution 1 (faster) -->1.82 sec
t=int(input())
for q in range(t):
  n,m=map(int,input().split())
  l=[0]*(m+1)
  for i in range(n):
    d,v=map(int,input().split())
    if l[d]<v:
        l[d]=v
  l.sort(reverse=True)
  print(l[0]+l[1])
        
  
# solution 2 slowler than 1 (2.63 sec)
t=int(input())
for q in range(t):
  n,m=map(int,input().split())
  l=[]
  for i in range(n):
    d,v=map(int,input().split())
    l.append([v,d])
  l.sort()
  s=0
  s=s+l[-1][0]
  p=l[-1][1]
  l.pop(-1)
  while True:
    if p==l[-1][1]:
        l.pop(-1)
    else:
        s=s+l[-1][0]
        print(s)
        break
    
        
    
  
    
  
