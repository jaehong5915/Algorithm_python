'''
지름길 
D 킬로의 고속도로에서
- N개의 지름길 
- min(고속도로 길이, 지름길 길이)
- dis[i]  = i 까지 최단거리

'''
import heapq

INF = int(1e9)
N, D = map(int,input().split())
data = [[] for _ in range(D+1)]
# data 초기화
for i in range(D):
    data[i].append((i+1,1))

for _ in range(N):
    start, end , length = map(int,input().split())
    if end > D:
        continue
    data[start].append((end,length))

distance = [INF] * (D+1)
distance[0] = 0

q = []
heapq.heappush(q,(0,0)) # 초기
while q:
    d, now = heapq.heappop(q)
    if distance[now] < d:
        continue
    for i in data[now]: #i[0] = end , i[1] = length/cost
        cost = i[1] + d 

        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

print(distance[D])