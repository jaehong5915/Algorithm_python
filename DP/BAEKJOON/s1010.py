'''
다리 놓기
N <= M
mCn -> fac[M]// (fac[N] * fac[M-N])

'''
# from math import factorial

dp = [1]
for i in range(1,30):
    dp.append(dp[i-1] * i)
print('::',dp)

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    rs = dp[m] // (dp[n] * dp[m-n])
    print(rs)
    # print(factorial(m)//(factorial(n) * factorial(m-n)))