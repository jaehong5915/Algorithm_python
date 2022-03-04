'''
스티커
변 공유 
a[i][j] = a[i-1][j] , a[i+1][j] , a[i][j-1], a[i][j+1] x
공유 안하는 스티커 최대값
'''
t = int(input())
for _ in range(t):
    n = int(input())
    data = []
    # data = [[] for _ in range(2)]
    for i in range(2):
        data[i] = list(map(int,input().split()))
    print(data)
    # dp = [[0] * n for _ in range(2)]
    # for i in range(2):
    #     for j in range(n):
            