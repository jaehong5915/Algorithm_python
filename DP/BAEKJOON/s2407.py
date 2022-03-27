'''
조합
nCm 출력하기
- n개 중 서로 다른 R개를 선택하되 순서를 고려하지 않는다.
nCr = n! / (r!*(n-r)!)
입력)
- n = 100, m = 6
'''
# 더 좋은 방법
'''
import math
up = math.factorial(n)
down = (math.factorial(n-m)) * (math.factorial(m))
print(up/down)
'''
n,m = map(int,input().split())
nfac = 1
rfac = 1
nrfac = 1
for i in range(1,n+1):
    nfac *= i
for j in range(1,m+1):
    rfac *= j
for i in range(1,n-m+1):
    nrfac *= i
print(nfac//(rfac*nrfac))