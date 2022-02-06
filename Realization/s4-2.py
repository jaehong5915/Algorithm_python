#3이 포함된 시간 경우의 수 찾기
## 전체 시간 나열하기
cnt = 0
n = int(input())

for h in range(n+1):
    for i in range(60):
        for j in range(60):
            if '3' in str(j) + str(i) + str(h):
                
                cnt +=1

print(cnt)
# print((cnt-1)*59*6)