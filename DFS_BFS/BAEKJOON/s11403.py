'''
경로 찾기
- 가중치 없는 방향 그래프 g, 모든 정점(i,j) 에 대해
i -> j 로가는 경로가 있는지 없는지 구하라
#입력
n (정점의 개수), 
그래프 인접행렬,

## 풀이
1. dfs ->  idx : +1
'''

import sys
sys.setrecursionlimit(100000)
rs =[]
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
def dfs(v):
    for i in range(n):
        if visit[i] == 0 and data[v][i] == 1:
            visit[i] = 1
            dfs(i)
for i in range(n):
    visit = [0 for _ in range(n)]
    dfs(i)
    print(' '.join(map(str,visit)))
    # print(*visit)