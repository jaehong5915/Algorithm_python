'''
visit 를 쓰고 ? 안 쓰고 ? 
섬의 개수
이동 -> 가로, 세로, 대각선
# 입력
1. 지도의 너비, 높이 주어짐
2. 지도(h) : 1은 땅, 0은 바다
# 해결
1. dfs -> 재귀 (아이스크림 개수와 동일한 방법)
'''

import sys
sys.setrecursionlimit(10**6)
# 이동 경로 - 가로,세로, 대각선

# w, h  = map(int,input().split())
# graph = []
# for _ in range(h):
#     graph.append(list(map(int,input().split())))
# cnt  = 0
    # for i in range(8):
    #     nx = x + dx[i]
    #     ny = y + dy[i]
dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]
def dfs(x,y):
    if w == 0 and h == 0:
        return False
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    # if graph[x][y] == 1:    ===dx . dy
    #     graph[x][y] = 0
    #     dfs(x+1,y+0)
    #     dfs(x+0,y+1)
    #     dfs(x-1,y+0)
    #     dfs(x+0,y-1)
    #     dfs(x-1,y-1)
    #     dfs(x+1,y+1)
    #     dfs(x+1,y-1)
    #     dfs(x-1,y+1)
    #     return True
    return False
while True:
    w, h  = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    cnt  = 0
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                cnt +=1 
    print(cnt)

        # for i in range(8):
        #     dfs(x+dx[i],y+dy[i])