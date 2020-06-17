#link:-https://www.codechef.com/JUNE20B/problems/EOEO
import math
t=int(input())
for q in range(t):
    s=0
    ts=int(input())
    if ts%2==1:
        print(ts//2)
    else:
        x=0
        if math.ceil(math.log2(ts))==math.floor(math.log2(ts)):
            print(0)
        else:
          le= int(math.log2(ts))+1
          i=2
          while 2**i<=ts:
            if ts % (2**i)== 2**(i-1):
              ts=ts-(2**(i-1))
              a=ts//(2**i)
              break
            i+=1
          print(a)
          
