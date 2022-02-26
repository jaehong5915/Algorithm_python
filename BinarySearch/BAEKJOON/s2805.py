'''
나무 자르기

입력)
n : 나무의 수, m : 필요한 나무의 길이
arr = 나무 길이

출력)
h - 필요한 나무 길이를 가져갈 수 있는 높이의 최댓값
'''
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree_list = sorted(list(map(int,input().split())))
start = 0
end = max(tree_list)
rs = 0
while start <= end:
    mid = (start+end)//2
    cnt = 0 #잘린 나무 
    for i in tree_list:
        if i > mid:
            cnt += i-mid
    if cnt >= m: # 더 많이 잘랐으므로 덜 잘라야함 (높이 +)
        # cnt == m 추가하는 이유
        start = mid + 1
        rs = mid
    else: # 덜 잘랐으므로 (높이 -)
        end = mid - 1
print(rs) 
# print(mid)
# end 출력하는 이유 -> 