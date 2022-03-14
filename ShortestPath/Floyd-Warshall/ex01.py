'''
플로이드 워셜
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우
- 2차원 배열 점화식 , DP 
1. 현재 확인하고 있는 노드를 제외하고
2. N - 1 개의 노드 중에서 서로 다른 노드 (A, B) 쌍을 선택
3. A -> 1 -> B 로 가는 비용 확인 후 dis[a][b] = min(A->B, A->1 + 1->B)
'''
inf = int(1e9)

n = int(input()) #노드 갯수
m = int(input()) #간선 갯수
# 2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[inf]*(n+1) for _ in range(n+1)]

# 1->1, 2->2 ,... 0으로 초기화
for i in range(1, n+1):
    for j in range(1,n+1):
        if i == j :
            graph[i][j] = 0

# 각 간선에 대한 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 
        if graph[a][b] == inf:
            print('도달 x ')
        else:
            print(graph[a][b], end=' ')
    print()
