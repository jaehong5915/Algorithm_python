'''
가장 긴 감소 수열 길이

'''

n = int(input())
data = list(map(int,input().split()))
# dp = [x for x in data]
dp = [0] * n
for i in range(n):
    for j in range(i+1,n):
        if data[i] > data[j]:
            dp[i] += 1
            dp[i] = data[j]
# for i in range(n-1,-1,-1):
#     for j in range(i-1,-1,-1):
#         if data[i] < data[j]:
#             dp[i] += 1
print(dp)
# print(max(dp))