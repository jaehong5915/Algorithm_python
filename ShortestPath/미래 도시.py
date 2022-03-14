'''
미래 도시
1번 회사 -> k번 회사 소개팅 -> X번 회사로 이동: 최소 이동
- 양방향 , 거리는 1
- 도착 못하면 -1
m
'''
inf = (1e9)
n, m = map(int,input().split())
graph = [[inf] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k  = map(int,input().split())
# distance = [[inf] * (n+1) for _ in range(n+1)]
#자기 자신 오는거 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(1,n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])
distance = graph[1][k] + graph[k][x]

# 모든 노드로 가기 위한 최단 거리를 출력
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
if distance >= inf:
    print(distance,-1)
# 도달할 수 있는 경우 거리를 출력
else:
    print(distance)