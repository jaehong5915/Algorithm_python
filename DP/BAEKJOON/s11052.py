'''
카드 구매하기
카드 i개가 포함된 카드팩의 가격 -> Pi
입력)
구매하려는 카드 수
p1 ~ pn : 팩 가격
출력)
카드 N 개를 갖기 위해 지불해야하는 금액 최대
--> price[idx] 값이 크면서 idx 값 작게
dp : 구매 팩에 따른 총 지불 금액
'''
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = p[0] # 카드 1개 경우
for i in range(2, n+1): #dp[i] 2, 3, 4 ,....n
    for j in range(1, i+1): # n = 3 ( dp[3-3] + j[3] ...)
        if dp[i] < dp[i-j] + p[j-1]: # dp.idx = p.idx - 1
            dp[i] = dp[i-j] + p[j-1]
print(dp[n])