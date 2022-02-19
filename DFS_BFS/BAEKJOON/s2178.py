'''
미로 탐색
(n,m) 까지 최소 (bfs)
bfs return -> data[n-1][m-1]

'''
from collections import deque

n, m = map(int,input().split())
data = [list(map(int,input())) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0<= ny < m:
                if data[nx][ny] == 1:
                    data[nx][ny] = data[x][y] + 1
                    q.append((nx,ny))
    
    return data[n-1][m-1]
    

print(bfs(0,0))