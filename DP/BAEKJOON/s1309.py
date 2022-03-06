'''
동물원
dp배열을 어떻게 구상할 것인가

ex n = 2
- n 2 -> 아무곳도 배치 X -> dp[i-1]
- n 1 -> 아무곳도 배치 x -> 전전 n이 아무것도 없을 경우의 2배 =  dp[i-2] * 2
- n 1, n 2인 곳 모두에 배치 -> 바로 이전 경우의 수에서 바로 전전 경우의 수 뺀 경우 = dp[i-1] - dp[i-2]
==> dp[i] = dp[i-1] + 2*dp[i-2] + (dp[i-1] - dp[i-2]) = 2*dp[i-1] + dp[i-2]
'''
n = int(input())
dp = [1, 3, 7]
for i in range(3,n+1):
    dp.append((dp[i-2] + (dp[i-1] * 2)) % 9901)
print(dp[n])
    