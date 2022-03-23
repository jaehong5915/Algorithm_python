#3이 포함된 시간 경우의 수 찾기
## 전체 시간 나열하기
cnt = 0
n = int(input())
h = n + 1 # 시간기준
for i in range(h):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
