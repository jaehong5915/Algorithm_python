from collections import deque


n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x,y,h):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if data[nx][ny] > h and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    q.append((nx,ny))
rs =[]
for k in range(max(map(max,data))):
    cnt = 0
    visit = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if data[i][j] > k and visit[i][j] == False:
                visit[i][j] = True
                bfs(i,j,k)
                cnt +=1
    rs.append(cnt)
print(max(rs))
