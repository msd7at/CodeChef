t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a,b=l[0],l[1]
    for i in range(2,n):
        s=[a,b,l[i]]
        a=min(s)
        s.remove(a)
        b=min(s)
    print(a+b)
    
"""
You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. 

The first line of each description consists of a single integer N.

The second line of each description contains N space separated integers - a1, a2, ..., aN respectively.

Output
For each test case, output a single line containing a single integer - the smallest possible sum for the corresponding test case.

Constraints
T = 105, N = 2 : 13 points.
T = 105, 2 ≤ N ≤ 10 : 16 points.
T = 1000, 2 ≤ N ≤ 100 : 31 points.
T = 10, 2 ≤ N ≤ 105 : 40 points.
1 ≤ ai ≤ 106
Example
Input:
1
4
5 1 3 4

Output:
4"""
