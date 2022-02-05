# 로프

n = int(input())
s =[]
result =[]
k =0
for i in range(n):
    s.append(int(input()))
s.sort(reverse=True)
for i in s:
    k += 1
    result.append(i*k)

print(max(result))