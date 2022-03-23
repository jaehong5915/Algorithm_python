# 왕실의 나이트
# ord -> a 97 b 98,,,104
n = input()
x=[-1,1,2,2,1,-1,-2,-2]
y=[2,2,1,-1,-2,-2,-1,1]
data1 = ord(n[0]) # a,b...h 가로좌표 97,98 ...104
data2 = n[1] # 세로 1,2,3,...8
cnt = 0
for i in range(len(x)):
    nx = x[i] + int(data1)
    ny = y[i] + int(data2)
    if 97<=nx<=104 and 1<=ny<=8:
        cnt +=1
print(cnt)
# n = list(map(str,input()))
# n[0] = ord(n[0])
# n[1] = int(n[1])
# cnt = 0

# x=[-1,1,2,2,1,-1,-2,-2]
# y=[2,2,1,-1,-2,-2,-1,1]

# for i in range(len(x)):
#     rx = n[0] + x[i]
#     ry = n[1] + y[i]

#     if rx<=104 and rx>=97 and ry>=1 and ry<=8:
#         cnt+=1 

# print(cnt)