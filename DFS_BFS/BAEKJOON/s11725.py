'''
https://d-cron.tistory.com/22   -> bfs, dfs
#트리의 부모 찾기
1. 루트 - 1 , n+1번 노드에 해당하는 부모노드 번호 출력
# dfs
 - 루트(1) dfs 탐색 시작 -> 1과 연결 node 중 방문 x 노드 방문 -> 
   visited 배열에 탐색 시작 node(부모) 저장
# bfs
 - 루트(1) 시작 -> q.append(1) while : -> 인덱스 now : 현재 방문 노드
  -> now 와 연결된 node 중 방문 x 노드들을 ans[nxt] 값에 now append
'''

from collections import deque
import sys
input = sys.stdin.readline

#dfs
n = int(input())
graph = [[] for _ in range(n+1)]
chk = [False] * (n+1)
ans = [1 for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)    

def dfs(v):
    chk[v] = True
    for i in graph[v]:
        if chk[i] == False:
            ans[i] = v
            dfs(i)
for i in range(1,n):
    dfs(i)
for i in range(2,len(ans)):
    print(ans[i])