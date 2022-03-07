'''
구간 합 구하기
'''

m,n = map(int,input().split())
data = []
for _ in range(m):
    data.append(list(map(int,input().split())))
for _ in range(n):
    a,b,c,d = map(int,input().split())
    sum = 0
    for i in range(a-1,c):
        for j in range(b-1,d):
            sum += data[i][j]
    print(sum)