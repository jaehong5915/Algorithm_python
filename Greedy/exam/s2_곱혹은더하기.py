'''
0, 1 의경우 덧셈 나머지 곱셈처리
'''
n = list(input())
n.sort(reverse=True)
k = list(map(int,n))
rs = k[0]
for i in range(1,len(k)):
    if k[i] == 0 or k[i] == 1:
        rs += k[i]
    else:
        rs *= k[i]
print(rs)