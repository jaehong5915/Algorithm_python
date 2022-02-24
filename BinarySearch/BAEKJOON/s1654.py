'''
랜선 자르기

입력)
- K = 이미 가지고 있는 랜선의 개수, n : 필요한 랜선의 개수
    K <= n
    - 이미 갖고 있는 랜선의 길이
- 기준점 : 랜선의 갯수
'''
import sys
input = sys.stdin.readline
k, n = map(int,input().split())
data = []
for _ in range(k):
    data.append(int(input()))
start = 1
end = max(data)
while start <= end:
        mid = (start + end)//2
        cnt = 0
        for i in data:
            cnt += i // mid
        if cnt >= n :
            start = mid + 1
        else:
            end = mid -1
print(end)
# 랜선 11개가 나와야함
# 나무자르기랑 비슷한 유형 <-> 
# target => 랜선 길이(?)

# 