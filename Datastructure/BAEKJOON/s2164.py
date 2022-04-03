'''
n, n-1, n-2, ... , 1
n == 4 > 4, 3, 2, 1
1. 제일 위 카드 버림 
2. 제일 위에 있는 카드를 맨 밑으로 보냄
3. 제일 마지막에 남게 되는 카드 출력
'''
# n = 4  : 4,3,2,1 > 1 버림 > 4,3,2 > 2 밑으로 >
# 2,4,3 > 3 버림 > 2,4 > 4 제일 밑으로 > 4, 2 > 2 버림 > 4
from collections import deque

n = int(input())
data = deque()
for i in range(n,0,-1):
    data.append(i)
while True:
    if len(data) == 1:
        break
    data.pop()
    data.appendleft(data.pop())
print(data[0])
# while True:
#     if len(data)== 1:
#         break
#     data.pop()
#     data.append(data.pop(0))
# print(data[0])
