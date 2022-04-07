'''
절댓값 힙
x 가 != 0 : 배열에 x 값을 추가
x == 0 : 배열에서 절댓값이 가장 작은 값 출력, 그 값 배열에서 제거
# 배열 비어있는데 0, 0을 출력
# 절대값 같으면 실제 더 작은 값 출력
'''
# 최소힙, 최대힙 풀어보기
import heapq
heap = []
n = int(input())
for _ in range(n):
    k = int(input())
    if k == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        if k > 0:
            heapq.heappush(heap, (k,k))
        elif k < 0:
            heapq.heappush(heap,(-k,k))
