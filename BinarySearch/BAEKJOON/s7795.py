'''
먹을 것인가 먹힐 것인가
f) - 시간초과 - ㅇ
'''
import sys
input= sys.stdin.readline
import bisect

# def search(start,end,target):
#     # 출력시 +1 해줘야함 인덱스 값으로 판별하기에
#     # 그러려면 중간값이 타겟보다 클 때 -1을 return 해줘야함
#     res = -1            
#     while start <= end:
#         mid = (start + end)//2
#         if b[mid] < target:
#             res = mid # list의 b가 타겟보다 작으면, 밑 인덱스는 다 작음  
#             start = mid + 1 # 다음 인덱스 확인을 위해
#         else:
#             end = mid -1
#     return res
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = sorted(list(map(int,input().split())))
    rs = 0
    for i in a:
        rs += (bisect.bisect_left(b,i))
    print(rs)
    # print(rs)
        #bisect.bisect(a,x) : b에 있는 i-1의 기존 항목 뒤에 
        # 오는 삽입 위치 반환
        # rs += (search(0,len(b)-1,i) +1)

