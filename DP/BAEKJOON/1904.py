'''
01 타일
1, 00 , 타일로 2진수
'''
n = int(input())
dp =[0,1,2,3,5]
for i in range(5,n+1):
    dp.append((dp[i-1]+dp[i-2])%15746)
print(dp[n])