'''
케빈 베이컨의 6단계 법칙
n 이 모든 사람을 만나는 수
입력)
n : 유저의 수(노드), m : 친구 관계의 수 (링크)

출력)
케빈 베이컨의 수가 가장 낮은 사람
(여러 명 -> 번호가 작은 사람)
'''
from collections import deque

n, m = map(int,input().split())
data = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
def bfs(v):
    num = [0] * (n+1)
    visit = [v]
    q = deque()
    q.append(v)
    while q:
        r = q.popleft()
        for i in data[r]:
            if i not in visit :
                visit.append(i)
                q.append(i)
                num[i] = num[r] + 1 # a에서 i로 1칸             
    return sum(num)
rs = []
rs1 = []
for i in range(1,n+1):
    rs.append(bfs(i))
print(rs.index(min(rs))+1)