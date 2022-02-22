'''
통계학 - s3
- 산술 : n개의 수들의 합을 n 으로 나눈 값
- 중앙 : n개의 수들을 오름차순 정렬 -> 그 중앙값
- 최빈 : n개의 수들 중 가장 많이 나타나는 값
- 범위 : n개의 수글 중 최댓값과 최솟값 차이
'''
from collections import Counter


n = int(input())
data = [[] for _ in range(n)]
for i in range(n):
    data[i] = int(input())
data.sort()

avg=0
mid=0
ran=0

avg = sum(data)/len(data)
mid = data[n//2]
cnt = Counter(data)
print('1::',cnt)
cnt = Counter(data).most_common(2)
print('2::',cnt)
ran = max(data) - min(data)
print(int(avg))
print(mid)
if len(cnt) >= 2:
    if cnt[0][1] == cnt [1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(ran)