'''
특정한 최단 경로
- 임의의 두 정점은 반드시 통과해야 한다.
1 -> N (주어진 두 정점을 통과해서 이동하는 방법)
입력)
N 노드, E 간선
E)
 - a 출발, b 도착, C 거리(비용)
반드시 거쳐야하는 정점 번호 v1, v2
'''
import heapq
import sys
input = sys.stdin.readline


inf = int(1e9)
N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
q = []


for _ in range(E):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))
    graph[end].append((start,cost))

v1, v2 = map(int,input().split()) # 반드시 거쳐야함
# 시작은 1번
def dijkstra(start):
    distance = [inf] * (N+1)
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        for i in graph[now]:
            min_cost = i[1] + cost
            if distance[i[0]] > min_cost:
                distance[i[0]] = min_cost
                heapq.heappush(q,(min_cost,i[0]))
            # v1, v2 를 지나야함 -> i[0] == v1, v2
    return distance
s_dij = dijkstra(1)
v1_dij = dijkstra(v1)
v2_dij = dijkstra(v2)
ans = min((s_dij[v1]+v1_dij[v2]+v2_dij[N]), (s_dij[v2] + v2_dij[v1] + v1_dij[N]))
if ans >= inf:
    print(-1)
else:
    print(ans)
