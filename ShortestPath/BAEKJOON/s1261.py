'''
알고스팟
- 이동방법 x+1,y / x-1,y/ x,y+1/ x,y-1
- 벽 부수기 가능
현재 (1,1)에 있는 운영진이 (n,m)으로 이동하려면 벽을 최소 몇개 부수어야 하는가
1. 이동이 가능하면 벽은 부수지 않는다.
2. 이동이 불가하면 (n,m 안에서 벽을 부수고 이동할 수 있다.)

3/19 ---- 다시 풀어야함
'''
from collections import deque

import heapq
import sys
input = sys.stdin.readline

inf = int(1e9)
n, m = map(int,input().split())
graph=[]
for _ in range(m):
    graph.append(list(map(int,input().strip())))
print(graph)
# graph[a][b] == 1 벽 , graph[a][b] == 0 이동 가능
# n,m 이동 ->
dx = [1,0,-1,0]
dy = [0,1,0,-1] 
visit = [[False] * m for _ in range(n)]
# distance = [[inf] * m for _ in range(n)]
cnt = 0
def bfs(v, h):
    global cnt
    q = deque()
    q.append((v,h))
    visit[v][h] == True
    # distance[v][h] == 0
    while q:
        x, y = q.popleft()
        # if 0<=x<m and 0<=y<n:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] == 0 and visit[nx][ny] == False:
                    visit[nx][ny] == True
                    if nx == m and ny == n:
                        return cnt
                        
                    q.append((nx,ny))
                    
                else:
                    graph[nx][ny] == 1
                    visit[nx][ny] == True
                    cnt += 1
                    if nx == m and ny == n:
                        break
                    q.append((nx,ny))
    
print(bfs(0,0))
