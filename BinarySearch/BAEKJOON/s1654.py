'''
랜선 자르기

입력)
- K = 이미 가지고 있는 랜선의 개수, n : 필요한 랜선의 개수
    K <= n
    - 이미 갖고 있는 랜선의 길이
'''
import sys
input = sys.stdin.readline
k, n = map(int,input().split())
data = []
for _ in range(k):
    data.append(int(input()))
tot = sum(data)
print(tot)
print(tot//n)