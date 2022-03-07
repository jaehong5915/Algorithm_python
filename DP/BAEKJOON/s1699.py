'''
제곱수의 합

제곱들의 합으로 표현
- 최소 개수
'''
## 12 안됨
import sys
input = sys.stdin.readline

n = int(input())
# cnt = 0
dp = [x for x in range(n+1)]
for i in range(1,n+1):
    for j in range(1,i):
        # 제곱수가 i보다 커지면 break
        if j**2 > i :
            break
        #작은 수부터 제곱 수를 지금 기준이 되는 수와 비교해서
        # 하나라도 있으면 그 제곱수 넣어주고 + 1
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1 #크면 최소항이 아니기에 이전 값에 + 1**2 경우를 더해서 +1
print(dp)