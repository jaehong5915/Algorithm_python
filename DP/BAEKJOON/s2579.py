'''
계단 오르기
규칙)
- 한번에 한계단 or 두계단
- 연속 세 개의 계단 x
- 마지막 도착 계단 밟아야함
'''

n = int(input())
score = []
dp = [0] * (n+1)
for _ in range(n):
    score.append(int(input()))
print(score)
dp[0] = score[0]
dp[1] = score[0] + score[1]
dp[2] = max(score[0] + score[2] , score[1] + score[2])
for i in range(3, n):
    dp[i] = max(dp[i-2] + score[i], dp[i-3]+score[i-1]+score[i])
print(dp[n-1])