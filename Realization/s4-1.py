#상하좌우
# (1,1) 시작 left(-1), right(+1), up(+1)

n = int(input())
x = 1
y = 1
plan = list(map(str,input().split()))
for i in plan:
    if i == 'L' and y>1:
        y -= 1
    elif i == 'R' and y<5:
        y += 1
    elif i == 'U' and x>1:
        x -= 1
    elif i == 'D' and x<5:
        x += 1
print(x,y)