'''
요세푸스 문제
q 로 풀기
'''
import sys
input = sys.stdin.readline
from collections import deque
n, k = map(int,input().split())
data = deque()
for i in range(1,n+1):
    data.append(i)
rs = []
while data:
    for i in range(k-1):
        data.append(data.popleft())
    rs.append(data.popleft())
print('<',end='')
for i in range(len(rs)-1):
    print(rs[i],end=', ')
print(rs[-1],end='')
print('>')
