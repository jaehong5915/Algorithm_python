'''
RGB 거리
집 N개, 빨 / 초/ 파 중 1
- 1번 집의 색은 2번 집의 색과 달라야 함
- N번 집의 색은 N-1번 집의 색과 달라야 함
- i(2<=N<=N-1)번 집의 색 i-1, i+1과 달라야 함

입)
집의 수 N
2 ~ N : 집별로 빨 - 초 - 파 칠하는 비용
출)
모든 집 칠하는 비용 최솟값
'''
n = int(input())
dp =[]
for i in range(n):
    dp.append(list(map(int,input().split())))
    # data[i] = list(map(int,input().split()))
    # dp -> 처음 색상을 빨 - 초 - 파 시작했을 때 비용 리스트
for i in range(1,len(dp)):
    # d[i-1] != d[i] 이용
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0] #빨간색 시작
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + dp[i][1] #빨간색 시작
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + dp[i][2] #빨간색 시작
#맨 마지막 행렬의 최소값
print(min(dp[n-1]))