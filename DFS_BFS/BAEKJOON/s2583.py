'''
영역 구하기
입력)
- m x n , k 개 직사각형
- k줄) 직사각형 왼쪽아래, 오른쪽위 꼭지점
- 세대 수 구하는 문제
- 0 2 4 4
  1 1 2 5
  4 0 6 2
'''
import sys
sys.setrecursionlimit(10000)
dx = [1,0,-1,0]
dy = [0,1,0,-1]

m, n, k = map(int,input().split())
data = [[0]*n for _ in range(m)]
for _ in range(k):
    a, b ,c,d= map(int,input().split())
    for j in range(a,c):
        for i in range(b,d):
            if data[i][j] == 0:
                data[i][j] = 1 
visit=[[False]*n for _ in range(m)]
def dfs(x,y):
    global cnt
    cnt +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < m and 0<= ny < n:
            if data[nx][ny] == 0 and visit[nx][ny] == False:
                visit[nx][ny] = True
                dfs(nx,ny)
rs= [] 
cnt =0
for i in range(m):
    for j in range(n):
        if data[i][j] == 0 and visit[i][j] == False:
            visit[i][j] = True
            cnt = 0
            dfs(i,j)
            rs.append(cnt)
print(len(rs))
rs.sort()
print(*rs)