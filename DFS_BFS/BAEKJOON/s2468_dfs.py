'''
안전 영역
1. 물에 잠기지 않는 영역의 최대갯수
1) 작은 수 부터 비교, rs[]에 삽입
i = 1 , 2 ,.... 9 -> rs.append() 
'''
import sys
sys.setrecursionlimit(100000)
n = int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
rs=[]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0 <= ny < n :
            if data[nx][ny] > h and visit[nx][ny] == False:
                visit[nx][ny] = True
                dfs(nx,ny,h)

ans = 1
# for k in range(10):
for k in range(max(map(max,data))):
    visit= [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] > k and visit[i][j] == False:
                visit[i][j] = True
                cnt += 1
                dfs(i, j, k) #조건 만족하면 -> 상 하 좌 우 재귀
    rs.append(cnt)
print(max(rs))