'''
구간 합 구하기
이중for문 시간초과
- 적은 연산 횟수로 합을 구하는 방법 구현 -> 매번 합을 구하는 과정의 시간을 단축시키자
- dp 배열 (x,y) 까지의 누적 합
'''

m,n = map(int,input().split())
data = []
dp = [[0] * (m+1) for _ in range(m+1)]
for _ in range(m):
    data.append(list(map(int,input().split())))
for i in range(m+1):
    for j in range(m+1):
        # dp(i,j) -배열 (i,j) 까지 누적합
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + data[i-1][j-1]    
for _ in range(n):
    a,b,c,d = map(int,input().split())
    print(dp[c][d]-dp[c][b-1]-dp[a-1][d]+dp[a-1][b-1])