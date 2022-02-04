# 큰 수의 법칙
## 배열의 크기 N, 숫자가 더해지는 횟수 M, 특정 인덱스 반복횟수 K

n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]
result  = 0
while True:
    for i in range(k):
        if m == 0 : break
        result += first
        m -= 1
    if m == 0 : break
    result += second
    m -=1

print(result)
