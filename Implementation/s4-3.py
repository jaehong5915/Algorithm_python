# 왕실의 나이트
# ord -> a 97 b 98,,,104
n = list(map(str,input()))
n[0] = ord(n[0])
n[1] = int(n[1])
cnt = 0

x=[-1,1,2,2,1,-1,-2,-2]
y=[2,2,1,-1,-2,-2,-1,1]

for i in range(len(x)):
    rx = n[0] + x[i]
    ry = n[1] + y[i]

    if rx<=104 and rx>=97 and ry>=1 and ry<=8:
        cnt+=1 

print(cnt)