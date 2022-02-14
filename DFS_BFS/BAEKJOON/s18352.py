'''
특정 거리의 도시 찾기 (단방향)
n : 도시 수, m : 도로 수, k : 거리 정보 , x : 출발
# bfs
'''
from collections import deque
import sys
input = sys.stdin.readline
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans = [-1]*(n+1)
ans[x] = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
q = deque()
q.append(x)
while q:
    now = q.popleft()
    for i in graph[now]:
        if ans[i] == -1 :
            ans[i] = 1 + ans[now]
            q.append(i)

for i in range(n+1):
    if ans[i] == k :
        print(i)
if k not in ans:
    print(-1)
