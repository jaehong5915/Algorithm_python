'''
a[0]*b[0] + a[1]*b[1] + ... + a[n-1] * b[n-1]
'''

a = list(map(int,input().split()))
b = list(map(int,input().split()))

rs = 0

for i in range(len(a)):
    rs += a[i]*b[i]
print(rs)
