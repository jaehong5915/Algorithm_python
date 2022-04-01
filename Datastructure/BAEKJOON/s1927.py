'''
최소 힙
입력)
n
0 - popleft(), print
그외 - 배열에 삽입
'''
import sys
input = sys.stdin.readline
import heapq

data = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(data) == 0:
            print(0)
        else:
            print(heapq.heappop(data))
    else:
        heapq.heappush(data,num)