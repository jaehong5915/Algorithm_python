'''
동전 ex) 1,1,2,3,9 를 활용하여 만들 수 없는 최소 금액
'''
from itertools import accumulate
n = int(input())
data = list(map(int,input().split()))
data.sort()
rs = 1
for i in data:
    if rs < i :
        break
    rs += i
print(rs)

