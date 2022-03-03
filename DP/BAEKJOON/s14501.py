'''
퇴사

'''
n = int(input())
time = []
money = []
dp = [0] * (n+1) # 이익 리스트 n 번째 돈 받는거
for _ in range(n):
    t,m = map(int,input().split())
    time.append(t)
    money.append(m)

for i in range(n-1,-1,-1):
    if time[i] + i > n : # i 일에 상담을 하는 것이 퇴사일을 넘기면 상담하지 않음.
        continue
        # dp[i] = dp[i+1] #   
    else:
        dp[i] = max(money[i] + dp[i+time[i]], dp[i+1]) # 상담을 하는 것과 상담을 하지 않는 것 최대값
print(max(dp))

# rs = 0
# for i in range(1,n+1):
#     for j in range(i):
#         dp[i] = max(dp[i], dp[j])

#         if j + time[j] == i:
#             dp[i] = max(dp[i], dp[j] + money[j])
#     rs = max(rs,dp[i])
# print(rs)