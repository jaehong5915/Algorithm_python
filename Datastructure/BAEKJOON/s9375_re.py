'''
패션왕 신해빈

'''
from collections import Counter
cnt = 0
n = int(input())
for _ in range(n):
    t = int(input())
    data = []
    for _ in range(t):
        kind, name = map(str,input().split())
        data.append(name)
    rs = Counter(data)    
    num = 1
    for i in rs:
        num *= rs[i] +1
    print(num-1)
