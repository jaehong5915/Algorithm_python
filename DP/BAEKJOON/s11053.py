'''
가장 긴 증가하는 부분 수열
dp - 바텀업 (이중포문)
dp - 횟수 
'''
n = int(input())
data = list(map(int,input().split()))
dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))