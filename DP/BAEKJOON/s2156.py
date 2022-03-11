'''
포도주 시식 == 계단 오르기
- 연속으로 3잔 마실 수 없음
입력)
N - 최대 마실 수 있는 포도주 양
경우)
- i 번째 포도주 마신 경우
    - i 먹고, ~ i-2 까지 / ~i-3, i-1 마심
- i 번째 x
    - ~ i-1 까지
'''
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))
dp =[0] * n
dp[0] = data[0]
if n > 1:
    dp[1] = data[0] + data[1] # 2번째 포도주
if n > 2:
    dp[2] = max(dp[1], data[0]+data[2],data[1]+data[2])
for i in range(3,n):
    dp[i] = max(dp[i-2]+data[i], dp[i-3]+data[i]+data[i-1], dp[i-1])
print(dp[n-1])