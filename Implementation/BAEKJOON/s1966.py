from collections import deque
# 프린터 큐
## 테스트케이스, 문서 갯수, 큐 위치, 중요도 입력

### 잘못된 풀이
# t = int(input())
# result =[]
# for i in range(t):
#     k = list(map(int,input().split()))
#     imp = list(map(int,input().split()))
#     a=imp[k[1]]
#     imp.sort(reverse=True)
#     if imp.count(a) > 1:
#         result.append(imp.count(a))
#     else:
#         result.append(imp.index(a)+1)
# for i in range(len(result)):
#     print(result[i])

t = int(input())
for i in range(t):
    n, x = map(int,input().split())
    que = deque(list(map(int,input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0
    while True:
        if que[0] == max(que):
            cnt+=1
            que.popleft()
            if idx_que.popleft() == x:
                print(cnt)
                break
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())