'''
dfs -> 원소 방문 처리, 방문하지 않은 원소 => dfs 재귀함수 실행
bfs -> 원소 방문 처리, 방문하지 않은 원소 => queue 삽입 후 pop
'''
from collections import deque
import sys
input = sys.stdin.readline
n, m, v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
chk = [False]*(n+1)
chk1 = [False]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dsf(v):
    chk[v] = True
    print(v, end=' ')
    for i in range(1,n+1):
        if chk[i] == False and graph[v][i] == 1:
            chk[i] = True
            dsf(i)

def bsf(v):
    q = deque()
    q.append(v)

    while q:
        chk1[v] = True
        v = q.popleft()
        print(v, end=' ')
        for i in range(1,n+1):
            if chk1[i] == False and graph[v][i] == 1:
                chk1[i] = True
                q.append(i)

dsf(v)
print()
bsf(v)