'''
# 나이트의 이동
t - 테스트 케이스, l - 체스판 한변 길이, 출발, 도착
1. bfs - 나이트 이동 경우의 수
2. while -> nx = cnt(1) + x / ny = cnt(1) +y
'''

from collections import deque
import sys
input = sys.stdin.readline

dx = [-2,-1,1,2,-2,-1,2,1]
dy = [1,2,2,1,-1,-2,-1,-2]

t = int(input())
for _ in range(t):
    l = int(input())
    x,y = map(int,input().split())
    z,w = map(int,input().split())
    graph = [[0]*l for _ in range(l)]
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if x == z and y == w:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    print(graph[z][w])