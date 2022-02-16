'''
모험가 길드
1. n 명수 / data 공포도
2. 공포도 x -> x명 그룹
s1) data 오름차순 -> data[0] = x , x명 -> data[0+x] = x , x명 ...
'''
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
data.sort()
cnt = 0
result = 0
# 공포도 낮은 순으로 그룹에 추가 시키기 -> 최대
for i in data:
    cnt +=1
    if i <= cnt:
        result += 1
        cnt = 0
print(result)
