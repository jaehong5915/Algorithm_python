# n명의 인출 시간 data[] 주어짐
# 최소 인출 시간

n=int(input())
data =list(map(int, input().split()))
data.sort()
sum1 = 0
result = 0
data2 =[]
for i in data:
    sum1 += i
    data2.append(sum1)
print(sum(data2))
