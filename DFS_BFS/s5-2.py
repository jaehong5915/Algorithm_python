# 미로 탈출
# 괴물 o -> o , 괴물 x -> 1
## 1. n,m / field 받기  2. 필드 벗어나면 False 3. 재귀 돌려서 괴물 없는 곳 탐색 

n, m = map(int,input().split())
field =[]
for i in range(n):
    field.append(list(map(int, input())))

def dsx(x,y):
    cnt =1
    if x <= -1 or x >= n or y <= -1 or y >= m :
        print('11111')
        return False
    
    if field[x][y] == 1:
        cnt += 1
        # field[x][y] += 1
        dsx(x,y+1)
        dsx(x,y-1)
        dsx(x-1,y)
        dsx(x+1,y)
        return cnt
    return False
for i in range(n):
    for j in range(m):
        result = dsx(i,j) 
print(result)