'''
상근이의 여행
입력)
T (테스트 케이스)
N (국가의 수), M(비행기 종류)
a, b (왕복 비행기)
'''
import sys

sys.setrecursionlimit(100000)
def dfs(v):
    global cnt
    for i in data[v]:
        if chk[i-1] == 0:
            chk[i-1] = 1
            if 0 not in chk:
                return cnt
            cnt += 1
            dfs(i)

t = int(sys.stdin.readline())
for _ in range(t):
    cnt = 0
    n,m = map(int,sys.stdin.readline().split())
    data=[[] for _ in range(n+1)]
    chk = [0] * (n)
    for _ in range(m):
        a,b = map(int,sys.stdin.readline().split())
        data[a].append(b)
        data[b].append(a)
    dfs(a)
    print(cnt)


