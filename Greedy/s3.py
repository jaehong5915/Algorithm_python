n,m = map(int, input().split())

result = []
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result.append(min_value)
print(max(result))