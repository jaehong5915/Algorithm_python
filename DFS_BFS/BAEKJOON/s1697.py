'''
숨바꼭질
위치  x = > 1초에 +- 1 씩 이동, 순간이동 2 * x
이동 위치 -> q에 넣고 
data [인덱스] = 인덱스까지 걸린 시간
'''
from collections import deque

n, k = map(int,input().split())
max = 10**5
data = [0] * (max+1)

def bfs():
    q = deque()
    q.append(n)

    while q:
        x= q.popleft()
        if x == k:
            print(data[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0<= nx <= max and data[nx] == 0:
                data[nx] = data[x] + 1
                q.append(nx)
bfs()