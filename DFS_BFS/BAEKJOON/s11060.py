'''
점프 점프
입력)
- N : 미로 칸 수
- Aj : N개
- dfs(인덱스)
'''
import sys
sys.setrecursionlimit(10000)


n = int(input())
data = list(map(int,input().split()))
pos= 0
cnt = 0
v= 0
visit = [False] * 100
def dfs(v):
    global pos
    global cnt
    if visit[v] == False:
        if pos >= n-1:
            return cnt
        visit[v] = True
        pos += data[v]
        cnt +=1
        dfs(pos)

print(dfs(0))