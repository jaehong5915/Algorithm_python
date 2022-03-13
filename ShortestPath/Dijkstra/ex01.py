'''
간단한 다익스트라 알고리즘 단계마다 방문하지 않은 노드 중
최단 거리 노드 선택을 위해 1차원 리스트의 모든 원소를 확인
'''

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split()) # 노드의 개수, 간선의 개수 입력
start = int(input()) #다익스트라 시작 노드
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1) # 해당 노드까지의 거리 리스트

for _ in range(m): #간선 개수
    a, b, c = map(int,input().split())
    #  a-> b로 가는 비용이 c
    graph[a].append((b,c))

#방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 return
def get_small_node():
    min_v = INF
    idx = 0 #가장 최단거리가 짧은 노드
    for i in range(1, n+1):
        if distance[i] < min_v and not visited[i]:
            min_v = distance[i]
            idx = i
    return idx

def dijkstra(start):
    #시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_small_node() #최단 거리가 짧은 노드 번호 리턴
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 짧음
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dijkstra(start) # 다익스트라 알고리즘 수행

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 해당 노드에 도달할 수 없으면 '무한'이라고 출력
    if distance[i] == INF:
        print('무한')
    else:
        print(distance[i])

