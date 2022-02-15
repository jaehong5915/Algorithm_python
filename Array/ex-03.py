'''
두 배열의 원소 교체
n - 배열 원소 수 , k - 바꾸기 횟수
'''
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break
print(sum(a))