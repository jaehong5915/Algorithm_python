import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
data = list(map(int,input().split()))
m = int(input())
chk = list(map(int,input().split()))
rs = Counter(data)

for i in chk:
    if i in rs:
        print(rs[i],end=' ')
    else:
        print(0, end=' ')
# for i in data:
#     if i in rs:
#         rs[i] += 1
#     else:
#         rs[i] = 1

# for i in chk:
#     if i in rs:
#         print(rs[i],end=' ')
#     else:
#         print(0, end=' ')