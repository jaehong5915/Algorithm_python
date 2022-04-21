'''
1. N일 동안의 물건의 매매가 예측 알고 있음
2. 하루에 최대 1만큼 구입 가능
3. 판매는 얼마든지 가능
ex) 매매가 1,2,3 -> 1,2 구입 -> 마지막날 팔면 3 이익
'''
t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    dp = [0] * n
    for i in range(0,n-1):
        for j in range()
