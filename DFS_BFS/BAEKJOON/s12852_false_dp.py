'''
1로 만들기
- x % 3 == 0 : x /= 3
- x % 2 == 0 : x /= 2
- else : x -= 1

입력) 
- 정수 x
출력)
- 연산을 하는 횟수 (최솟값)
- 과정
'''
from collections import deque

n = int(input())
cnt = []
def bfs():
    q = deque()
    q.append(n)
    cnt.append(n)
    while q:
        r = q.popleft()
        if r == 1:
            break
        if (r-1)%3 == 0:
            r -= 1
            q.append(int(r))
            cnt.append(int(r))
        elif r%2 != 0 and r%3 !=0:
            r -= 1
            q.append(int(r))
            cnt.append(int(r))
        elif r%3 == 0:
            r /= 3
            q.append(int(r))
            cnt.append(int(r))
        else:
            r /= 2
            q.append(int(r))
            cnt.append(int(r))
bfs()
print(len(cnt)-1)
print(*cnt)

        