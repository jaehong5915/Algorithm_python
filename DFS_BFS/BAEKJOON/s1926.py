"""
1. 아이디어
- 2중 for => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신
2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 >> 가능!
3. 자료구조
- 그래프 전체 지도 : int[][]
- 방문 : bool[][]
- Queue(BFS)
"""
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    rs = 1
    q = deque()
    q.append((x,y))
    while q:
        ex, ey = q.popleft()
        print('q:::',q)
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<n and 0<=ny<m: #좌표값이 그래프 안이면서
                if map[nx][ny] == 1 and chk[nx][ny] == False:
                    rs +=1
                    chk[nx][ny] = True #다시 탐색 못하게
                    q.append((nx,ny))
                    print('q.append:::',q)
    return rs
cnt = 0
maxv = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt +=1
            maxv = max(maxv, bfs(i,j))
print(cnt)
print(maxv)