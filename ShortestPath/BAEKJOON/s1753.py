'''
최단 경로
v 노드, e 간선
start = 시작노드
u -> v (w)
출력 ) 최소 경로
'''
import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
S = int(input())
INF = int(1e9)
data = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int,input().split())
    data[u].append((v,w))


q = []
heapq.heappush(q,(0,S))
distance[S] = 0

while q:
    co, now = heapq.heappop(q)
    if distance[now] < co:
        continue
    for i in data[now]: #i[0] 도착, i[1] 비용
        cost = i[1] + co
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost, i[0]))

for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])