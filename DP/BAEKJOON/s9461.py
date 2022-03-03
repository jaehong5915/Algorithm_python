'''
파도반 수열
'''
t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1,1,1,2,2,3,4]
    for i in range(7,n+1):
        dp.append(dp[i-2] + dp[i-3])
    print(dp[n-1])
        
