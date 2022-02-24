'''
예산
- 이진 탐색 : 기준점 -> 최대 배정 예산
- 지방의 요청 금액에 배정될 수 있으면 배정
- 안되면 상한액 책정하여 요청액과 비교 후 배정
입력)
- n : 지방의 수 , 
    지방(n)
- m : 총 예산
'''
n = int(input())
data = list(map(int,input().split()))
m = int(input())
start = 1
end = max(data)
while start<=end:
    cnt = 0
    mid = (start+end)//2
    for j in data:
        if mid > j :
            cnt += j
        else:
            cnt += mid
    if m >= cnt:
        start = mid + 1
    else:
        end = mid - 1
print(end)

