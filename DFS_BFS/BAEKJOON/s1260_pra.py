# n, m, v -> n : 노드  m : 간선 v: 시작점
# dfs, bfs 구하기
'''
1. n,m,v -> graph ( 00000 ...) -> visited [Fasle] * n+1
2. bfs, dfs -> 
'''
from collections import deque

n,m,v = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
dfs_visit = [False] * (n+1)
bfs_visit = [False] * (n+1)
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] == 1
    graph[b][a] == 1
# v 시작 노드
def dfs(v):
    dfs_visit[v] = True
    print(v, end= ' ')
    for i in range(1,n+1):
        if dfs_visit[i] == False and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    bfs_visit[v] = True
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1,n+1):
            if bfs_visit[i] == False and graph[x][i] == 1:
                bfs_visit[i] = True
                q.append(i)

dfs(v)
print()
bfs(v)














# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m, v = map(int, input().split())
# graph = [[0]*(n+1) for _ in range(n+1)]
# # visited = [False]*(n+1) #visited 하나로 가능한지?
# # visited1 = [False]*(n+1)
# #양방향 그래프
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a][b] = 1
#     graph[b][a] = 1

# def dfs(v):
#     visited[v] = True
#     print(v, end=' ')
#     for i in range(1,n+1):
#         if visited[i] == False and graph[v][i] == 1:
#             dfs(i)

# def bfs(v):
#     visited[v] = True
#     q = deque()
#     q.append(v)
#     while q:
#         v = q.popleft()
#         print(v, end=' ')
#         for i in range(1, n+1):
#             if visited[i] == False and graph[v][i] == 1:
#                 q.append(i)
#                 visited[i] = True
# visited = [False]*(n+1)                
# dfs(v)
# visited = [False]*(n+1)
# print()
# bfs(v)