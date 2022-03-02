'''
1,2,3 더하기

정수 n이 주어졌을 때, n 을 1,2,3의 합으로 나타내는 방법의 수 
'''
import math


t = int(input())
for _ in range(t):
    n = int(input())
    d=[0,1,2,4]
    for i in range(4,n+1):
        d.append(d[i-1] + d[i-2] + d[i-3])

    print(d[n])
