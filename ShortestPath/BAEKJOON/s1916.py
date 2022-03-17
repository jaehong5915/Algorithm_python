'''
최소비용 구하기
- N개의 도시, M개의 버스

입력)
n - 도시 m - 버스
버스 정보
    - 출발, 도착, 비용
출발, 도착
출력)
출발 도시에서 도착 도시까지 가는데 드는 최소 비용
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input()) #도시, 노드
m = int(input()) # 버스 갯수
bus = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int,input().split())
    bus[start].append((end,cost))
S, E = map(int,input().split()) # 출발점, 도착

distance = [INF] * (n+1)
distance[S] = 0
q = []


heapq.heappush(q,(0,S))
while q:
    cost, now = heapq.heappop(q)
    if distance[now] < cost:
        continue
    for i in bus[now]:
        min_cost = i[1] + cost
        if distance[i[0]] > min_cost :
            distance[i[0]] = min_cost
            heapq.heappush(q,(min_cost,i[0]))

print(distance[E]) 