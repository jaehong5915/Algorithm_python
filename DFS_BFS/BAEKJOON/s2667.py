'''
Q) 그래프에서 1인 집끼리 이어진 범위를 구하고 , 각각의 갯수를 센다

1. 정사각형 그래프 크기 및 입력
    1). gra , chk, dx,dy
2. 총 단지수 출력
    1). bfs-dx,dy
'''
import sys
input = sys.stdin.readline

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j,i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)
