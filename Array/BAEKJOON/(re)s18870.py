'''
좌표 압축
1000 999 1000 999 1000 999 -> 이 경우에서 cnt = 1로 출력 돼야 함
data1 = list(set(data)) -> set()을 통해 중복 제거
시간초과 해결을 위해 딕셔너리 사용 -> Value 호출
'''

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data1 = list(set(data))
data1.sort()
d = {data1[i] : i for i in range(len(data1))}
for i in data:
    print(d[i], end=' ')

