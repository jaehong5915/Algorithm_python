'''
맥주 마시면서 걸어가기
- 50M 마다 맥주 1병, 최대 맥주 20병 -> 최대 1000M 이동
- 편의점들리면 맥주 최대치로 (20)
- 집- 편의점 - 페스티벌 이동거리 > 1000M -> Sad else: happy
입력)
- t (테스트 케이스)
- 편의점 갯수
- n+2
    - 집, 편의점(*n) , 페스티벌 좌표
    - 편의점에서 다시 재귀로 dfs

1. 집 - 페스티벌 거리로 Happy
2. 편의점 따로 받고, 편의점 방문여부 -> 현위치와 편의점 거리
3. 편의점 방문시 방문처리, 큐에 위치 추가

'''
from collections import deque

def bfs():
    q = deque()
    q.append(home) # 큐에 시작위치 넣기
    chk = [False] * n #편의점 방문수 체크
    while q:
        x, y = q.popleft()
        if abs(x-fest[0]) + abs(y-fest[1]) <= 1000:
            # 집 -> 페스티벌 순수 거리 1000 이하 -> True
            return True
        for i in range(n):
            if chk[i] == False:
                cx, cy = conv[i] # 편의점 좌표 큐에 넣고 
                if abs(x-cx) + abs(y-cy) <= 1000:
                    chk[i] = True # 방문 체크
                    q.append((cx,cy))
    return False # 중간에 True 되지 않는경우 -> 거리가 1000 초과 
t = int(input())
for _ in range(t):
    n = int(input())
    conv=[]
    home = list(map(int,input().split()))
    for _ in range(n):
        conv.append(list(map(int,input().split())))
    fest = list(map(int,input().split()))
    if bfs() == True:
        print('happy')
    else:
        print('sad')



