#상하좌우
# (1,1) 시작 left(-1), right(+1), up(+1)

n = int(input()) # N x N
#(x,y) L : (x-1,y) R : (x+1,y) U : (x,y-1) D:(x, y+1)
data =list(map(str,input().split()))

x,y = 1,1  # 1<= x, y <= 5 
for i in data:
    if i == 'L' and x-1 >= 1:
        x -= 1
    elif i == 'R' and x+1 <= 5:
        x +=  1
    elif i == 'U' and y-1>= 1:
        y -= 1
    elif i == 'D' and y + 1 <= 5:
        y += 1
print(y,x)






# n = int(input())
# x = 1
# y = 1
# plan = list(map(str,input().split()))
# for i in plan:
#     if i == 'L' and y>1:
#         y -= 1
#     elif i == 'R' and y<5:
#         y += 1
#     elif i == 'U' and x>1:
#         x -= 1
#     elif i == 'D' and x<5:
#         x += 1
# print(x,y)