# 1이 될 때까지
## N에서 1을 뺀다.  / N을 k로 나눈다.(N이 K로 나누어떨어질 때만 선택 가능.)
### 우선순위 나누는 것 (나누어 떨어질 때까지 1번 수행)

# n,k = map(int, input().split())
# count = 0
# while True:
#     if n % k ==0:
#         n //= k
#         count +=1;
#     else:
#         n -= 1    
#         count +=1
#     if n == 1 : break
# print(count)


n, k = map(int,input().split())
cnt = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

