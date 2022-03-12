'''
상자 넣기
가장 길게 증가하는 리스트 길이
'''

n = int(input())
data = [0] + list(map(int,input().split()))
dp = [0] * (n+1) # dp idx번을 택했을 때 가장 긴 길이
# dp[1] = 1
for i in range(1,n+1):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))