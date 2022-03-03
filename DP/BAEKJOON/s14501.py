'''
퇴사

'''
n = int(input())
time = []
money = []
dp = [0] * n
for _ in range(n):
    t,m = map(int,input().split())
    time.append(t)
    money.append(m)
for i in range(n):
    j = 0
    earn = 0
    while j < n :
        if j == n-1:
            break
        earn += money[j]
        j += time[j]

    dp[i] = earn
print(max(dp))