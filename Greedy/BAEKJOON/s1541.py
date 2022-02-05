#잃어버린 괄호

a = input().split('-')
result = 0
plus=0
minus=0
for i in a[0].split('+') :
    plus += int(i)
for i in a[1:]:
    k = i.split('+')
    for j in k:
        minus += int(j)

print(plus - minus)

        