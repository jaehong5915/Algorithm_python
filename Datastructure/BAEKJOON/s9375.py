'''
패션왕 신해빈
4/10 다시 풀기
'''
from collections import Counter
cnt = 0
n = int(input())
for _ in range(n):
    t = int(input())
    data = []
    for _ in range(t):
        a,  b = map(str,input().split())
        data.append(b)
    rs = Counter(data)    
    pr_rs = 1
    for i in rs:
        pr_rs *= rs[i] +1
    print(pr_rs-1)
