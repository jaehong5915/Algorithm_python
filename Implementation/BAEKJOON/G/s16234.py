'''
인구이동
입력)
N, L, R (NxN , L<=x <= R )
NxN
출력)
인구이동이 며칠 발생하는지 (몇번)

-- 이동 상하좌우
'''
from collections import deque
import sys
input = sys.stdin.readline

n, l, r = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    visit[i][j] = True
    q = deque()
    q.append((i,j))
    pos = []
    pos.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == False:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    visit[nx][ny] = True
                    q.append((nx,ny))
                    pos.append((nx,ny))
    return pos

cnt = 0
while True:
    visit = [[False] * n for _ in range(n)]
    ismove = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                pos = bfs(i,j)
                if len(pos) > 1:
                    ismove = True
                    num = sum(data[x][y] for x,y in pos)//len(pos)
                    for x,y in pos:
                        data[x][y] = num
    if ismove == False:
        break
    cnt += 1

print(cnt)