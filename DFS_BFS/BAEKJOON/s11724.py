'''
1. dfs
2. 정점n, 간선 m
3. 무방향
    - append 로 그래프 삽입하기
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
chk = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    chk[v] = True

    for i in graph[v]:
        print('i:::',i)
        if chk[i] == False:
            chk[i] = True
            dfs(i)
cnt = 0
for i in range(1, n+1):
    if chk[i] == False:
        dfs(i)
        cnt +=1
print(cnt)

