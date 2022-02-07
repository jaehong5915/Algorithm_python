# 덩치
## 덩치가 더 큰 사람 n명 -> n+1 등

n = int(input())
data =[]
for i in range(n):
    data.append(list(map(int,input().split())))
for i in data:
    cnt =1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            cnt +=1 
    print(cnt, end=' ')