'''
t = 1 경우 먼저
dfs -> 상하좌우 더이상 1 없으면 return
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(x,y):
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph=[[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a, b = map(int,input().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt +=1
    print(cnt)