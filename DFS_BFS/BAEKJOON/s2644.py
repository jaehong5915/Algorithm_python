'''
촌수계산
입력)
- n 사람 수
- 촌수 계산 사람 번호
- 부모 자식간 관계 수
- 관계 나타내는 번호(x,y) (간선)
    x = y 의 부모노드

출력)
- 친척 관계가 전혀 없으면 '-1'
==> 몇번 노드를 지나는지 cnt
'''
n = int(input())
p, c = map(int,input().split())
m = int(input())

data= [[] for _ in range(n+1)]
chk = [0] *(n+1)
for _ in range(m):
    x, y = map(int,input().split())
    data[x].append(y)
    data[y].append(x)

def dfs(c):
    for i in data[c]:
        if chk[i] == 0:
            chk[i] = chk[c] + 1
            dfs(i)
        
dfs(c)
if chk[p] > 0:
    print(chk[p])
else:
    print(-1)