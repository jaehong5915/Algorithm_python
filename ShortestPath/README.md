# 최단 경로

<aside>
💡 **다익스트라 최단 경로 알고리즘 - 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드를 선택함**

</aside>

- 매 상황에서 가장 적은 비용의 노드 선택 ⇒ 반복
- 한번 처리된 노드의 최단거리는 불변
    1. 출발 노드를 설정한다.
    2. 최단 거리 테이블 초기화한다. [모든 거리 무한 설정, 자기 자신에 대한 노드 (1 → 1) ‘0’ 으로
    3. 방문하지 않은 노드 중에서 **최단 거리가 가장 짧은 노드를 선택한다  : 그리디**
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블 갱신 (data[i] = data[a] + 거리)
    5.  3 과 4번 반복

```python

#다익스트라 복잡도 - O(V^2)

import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값

n, m = map(int,input().split()) # n :노드 , m: 간선
start = int(input()) # 시작노드
graph = [[] for _ in range(n+1)] #노드에 대한 연결 정보
visit = [False] * (n+1) #방문 체크
distance = [INF] * (n+1) #최단 거리 테이블을 모두 무한으로 초기화 (초기 세팅)

for _ in range(m):
	a,b,c = map(int,input().split()) # a -> b 로 가는 비용 c
	graph[a].append((b,c))

def smallest(): #방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 Idx 반환
	min_v = INF
	idx = 0
	for i in range(1, n+1):
		if distance[i] < min_v and visit[i] == False:
			min_v = distance[i]
			idx = i
	return idx

def 다익스트라(start):
	# 시작노드 초기화  
	distance[start] = 0
	visit[start] = True
	for j in graph[start]: # j (a,b) a: 도착노드, b: 거리
		distance[j[0]] = j[1]
	for i in range(n-1):
		now = smallest()
		visit[now] = True
	for j in graph[now]:
		cost = distance[now] + j[1] # 거리 더해줌
		if cost < distance[j[0]]:
			distance[j[0]] = cost

다익스트라(start)

for i in range(1,n+1):
	if distance[i] == INF : # 도달할 수 없으면
		print('도달 x')
	else:
		print(distance[i])

============================================================
# 개선된 다익스트라 
## 힙 자료구조 사용

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값

n, m = map(int,input().split()) # n :노드 , m: 간선
start = int(input()) # 시작노드
graph = [[] for _ in range(n+1)] #노드에 대한 연결 정보
visit = [False] * (n+1) #방문 체크
distance = [INF] * (n+1) #최단 거리 테이블을 모두 무한으로 초기화 (초기 세팅)

for _ in range(m):
	a,b,c = map(int,input().split()) # a -> b 로 가는 비용 c
	graph[a].append((b,c))

def 다익스트라(start):
	q = []
	heapq.heappush(q, (0,start))
	distance[start] = 0
	while q: # 큐가 비어있지 않다면
	# 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
	dist, now = heapq.heappop(q)
	# 현재 노드가 이미 처리된 적이 있는 노드라면 무시
	if distance[now] < dist:
		continue
	# 현재 노드와 연결된 다른 인접한 노드들을 확인
	for i in graph[now]:
		cost = dist + i[1]
		# 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
		if cost < distance[i[0]]:
			distance[i[0]] = cost
			heapq.heappush(q, (cost,i[0]))
다익스트라(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
	for i in range(1,n+1):
		if distance[i] == INF : # 도달할 수 없으면
			print('도달 x')
		else:
			print(distance[i])
```

<aside>
💡 **플로이드 워셜 알고리즘**

</aside>

-