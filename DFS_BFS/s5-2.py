from collections import deque
# 미로 탈출, 가까운 노드 -> 큐
# 괴물 o -> o , 괴물 x -> 1
## 1. n,m / field 받기  2. 필드 벗어나면 False 3. 재귀 돌려서 괴물 없는 곳 탐색 

n,m = map(int,input().split())
field =[]
for _ in range(n):
    field.append(map(int,input()))

#이동 거리
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

print(bfs(0,0))