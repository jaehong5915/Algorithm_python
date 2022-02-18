'''
안전 영역
1. 물에 잠기지 않는 영역의 최대갯수
1) 작은 수 부터 비교, rs[]에 삽입
i = 1 , 2 ,.... 9 -> rs.append() 
'''

n = int(input())
data=[]
data1 =[]

for i in range(n):
    data.append(list(map(int,input().split())))
    

for i in range(n):
    for j in range(n):
        data1.append(data[i][j])
high = min(data1)

for i in range(n):
    for j in range(n):
        if high > 9:
            break
        else:
            if data[i][j] > high:
                data[i][j] = 1
            else:
                data[i][j] = 0

def dfs(x,y):
    
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if data[x][y] == 1:
        data[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)    
        return True
    return False
cnt = 0
rs=[]
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            cnt += 1
            high += 1
rs.append(cnt)
print(rs)