'''
가장 큰 수열
'''

n = int(input())
data = list(map(int,input().split()))
dp = [x for x in data]
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + data[i]) ##음수
            # dp[i] = dp[j] + data[i]
print(max(dp))