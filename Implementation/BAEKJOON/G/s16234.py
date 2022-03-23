'''
인구이동
입력)
N, L, R (NxN , L<=x <= R )
NxN
출력)
인구이동이 며칠 발생하는지 (몇번)

-- 이동 상하좌우
'''
import sys
input = sys.stdin.readline
from collections import deque

dx=[1,0,-1,0]
dy=[0,1,0,-1]
n,L,R = map(int,input().split())
data =[]
for _ in range(n):
    data.append(list(map(int,input().split())))
peo = 0
def bfs(i,j):
    global peo
    visit[i][j] = True
    q = deque()
    q.append((i,j))
    rs = []
    rs.append((i,j))
    peo += data[i][j]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] == False:
                if L<=(abs(data[nx][ny] - data[x][y]))<=R:
                    visit[nx][ny] = True
                    q.append((nx,ny))
                    rs.append((nx,ny))
                    peo += data[nx][ny] # 집단 
    return rs
cnt = 0
while True:
    ismove = False
    visit = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                result = bfs(i,j)
                if len(result) > 1: # 이동함
                    ismove = True
                    # people1 = peo//len(result)
                    # print(people)
                    # print(sum(data[x][y] for x,y in result))
                    people = sum(data[x][y] for x,y in result) // len(result)
                    for x,y in result:
                        data[x][y] = people
    if ismove == False:
        break
    cnt += 1
print(cnt)