'''
두 수의 합
n 개의 서로 다른 양의 정수 , 자연수 x -> x = a[i] + a[j] 쌍의 갯수
시간 제한 -> while , 포인터 접근
'''
import sys
input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int,input().split())))
x = int(input())

left , right = 0 , n-1
cnt = 0
while left < right:
    tot = data[left] + data[right]
    if tot == x:
        cnt +=1
        left +=1
    elif tot > x:
        right -= 1
    else:
        left +=1
print(cnt)