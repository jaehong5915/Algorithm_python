'''
#바이러스
- dfs -> 연결되면 바이러스 감염 cnt+1
- n 노드 m 간선
'''
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
chk = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
v =1
cnt = 0
def dsf(v):
    global cnt
    chk[v] = True
    cnt +=1
    for i in range(1,n+1):
        if chk[i] == False and graph[v][i] == 1:
            chk[i] = True
            dsf(i)
            
    return cnt-1
print(dsf(v))