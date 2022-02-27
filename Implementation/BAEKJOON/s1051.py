'''
숫자 정사각형
입력)
n, m -> n X m 크기 직사각형 
출력)
n X m 크기 직사각형 
-> 꼭짓점에 쓰인 수가 모두 같은 가장 큰 정사각형
꼭짓점 다 같은 수 있으면 (i*j)
'''
n,m = map(int,input().split())
data =[]
for _ in range(n):
    data.append(list(map(int,input())))
rs = []
for i in range(n):
    for j in range(m):
        if data[i][i] == data[i][j] and data[i][i] == data[j][i] and data[i][i] == data[j][j]:
            rs.append(abs((j-i))*abs((j-i)))
print(rs)
