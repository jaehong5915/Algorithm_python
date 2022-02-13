import sys
input = sys.stdin.readline

n=int(input())
map=[]
for i in range(n):
    map.append(map(int,input()))
# map = [list(map(int,input())) for _ in range(n)]

def dsf(x,y):

    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if map[x][y] == 1:
        map[x][y] = 2
        dsf(x-1,y)
        dsf(x+1,y)
        dsf(x,y-1)
        dsf(x,y+1)
        return True
    return False
cnt = 0
for i in range(n):
    for j in range(m):
        if dsf(i,j) == True:
            cnt +=1
print(cnt)