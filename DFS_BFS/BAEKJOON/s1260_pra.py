# n, m, v -> n : 노드  m : 간선 v: 시작점
# dfs, bfs 구하기
'''
1. n,m,v -> graph ( 00000 ...) -> visited [Fasle] * n+1
2. bfs, dfs -> 
'''
from collections import deque
n,m,v = map(int,input().split())
graph = [[0]* (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
# def dfs(v):
#     visited[v] = True
#     print(v, end=' ')
#     for i in range(1,n+1):
#         if visited[i] == False and graph[v][i] == 1:
#             dfs(i)
def dfs(v):
    visit[v] == True
    print(v,end=' ')
    for i in range(1,n+1):
        if graph[v][i] == 1 and visit[i] == False:
            dfs(i)
def bfs(v):
    visit[v] = True
    q = deque()
    q.append(v)
    while q:
        k = q.popleft()
        print(k, end=' ')
        for i in range(1, n+1):
            if visit[i] == False and graph[k][i] == 1:
                visit[i] = True
                q.append(i)
visit=[False] * (n+1)
dfs(v)
print()
visit=[False] * (n+1)
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