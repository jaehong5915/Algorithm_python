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
chk = min(n,m)
for _ in range(n):
    data.append(list(map(int,input())))
rs = []
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(chk):
            if i+k < n and j+ k<m:
                if data[i][j] == data[i][j+k]:
                    if data[i][j] == data[i+k][j]:
                        if data[i][j] == data[i+k][j+k]:
                            ans = (k+1)**2
                            rs.append(ans)
                            ans = 0
print(max(rs))
