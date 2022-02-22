'''
숫자 카드
'''
from collections import Counter
n = int(input())
data = list(map(int,input().split()))
m = int(input())
chk = list(map(int,input().split()))

c = Counter(data)
rs = []
for i in chk:
    if i in c:
        rs.append(1)
    else:
        rs.append(0)
print(*rs)
