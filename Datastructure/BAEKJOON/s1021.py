'''
회전하는 큐
n : 큐의 크기, m : 뽑아 내려 하는 수의 개수
뽑아내려한느 수의 위치 순서대로 주어짐
'''
# - popleft()
# - q.append(popleft())
# -q.leftappend(pop())
from collections import deque

n, m  = map(int,input().split())
data = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
cnt = 0
for i in data:
    while True:
        if i == q[0]:
            q.popleft()
            break
        else:
            if q.index(i) > len(q) /2:
                while i != q[0]:
                    q.appendleft(q.pop())
                    cnt +=1
            else:
                while i != q[0]:
                    q.append(q.popleft())
                    cnt +=1
print(cnt)