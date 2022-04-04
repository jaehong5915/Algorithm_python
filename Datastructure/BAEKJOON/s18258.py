'''
큐 2
- push X : X를 큐에 넣기
- pop : 큐에서 가장 앞 정수 빼고, 출력
- size : 큐에 정수 개수
- empty : 비면 1, 아니면 0
- front : 큐의 가장 앞 정수 출력, 없으면 -1
- back : 가장 뒤 정수 출력, 없으면 -1
'''
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
rs = deque()
for _ in range(n):
    k = input()
    if 'push' in k:
        data = k.split()
        rs.append(data[1])
    elif 'pop' in k:
        if len(rs) == 0 :
            print(-1)
            
        else:
            print(rs.popleft())
    elif 'size' in k:
        print(len(rs))
    elif 'empty' in k:
        if len(rs) == 0:
            print(1)
            
        else:
            print(0)
    elif 'front' in k:
        if len(rs) == 0:
            print(-1)
        else:
            print(rs[0])
    elif 'back' in k:
        if len(rs) == 0:
            print(-1)
        else:
            print(rs[-1])
