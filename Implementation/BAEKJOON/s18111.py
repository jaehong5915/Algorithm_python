'''
마인크래프트
1. (i,j)의 가장 위에있는 블록을 제거하여 인벤토리에 넣음 -1
2. 인벤토리에서 블록 하나를 꺼내어 (i,j) 가장 위에 놓는다. + 1
1번 작업 2초
2번 작업 1초
- 땅고르기 작업에 걸리는 최소 시간과 그 땅의 높이 출력
- B (블록 갯수)
- N, M (세로, 가로)

'''
from collections import deque

n,m,b = map(int,input().split())
dx = [1,0,-1,0]
dy = [0,1,0,-1]

data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
visit = [[False]*n for _ in range(m)]
def bfs(i,j):
    cnt = 0
    visit[i][j] = True
    q = deque()
    q.append((i,j))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx < n and 0<=ny<m and visit[nx][ny] == False:
                if data[nx][ny] == data[x][y]:
                    visit[nx][ny] = True
                    q.append((nx,ny))
                elif data[x][y] > data[nx][ny]:
                    data[x][y] -= 1
                    cnt +=2
                    b += 1
                    visit[nx][ny] = True
                    q.append((nx,ny))
                elif data[x][y] < data[nx][ny]:
                    data[x][y] += 1
                    cnt +=1
                    b -= 1
                    visit[nx][ny] = True
                    q.append((nx,ny))
    return cnt
rs = []
for i in range(n):
    for j in range(m):
        rs.append(bfs(i,j))
print(rs)