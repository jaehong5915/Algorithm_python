# 자료구조
- heapq

```python
    # 자바의 PriorityQueue 클래스 
    # 최소 힙 -> heapq 모듈을 통해 원소 추가, 삭제한 리스트
    # heappush(), heappop()
    test = []
    heapq.heappush(test, 4)
    heapq.heappush(test, 3)
    print(test) => [3,4] # 자동 오름차순

    #가장 작았던 3 삭제되어 리턴
    print(heapq.heapop(test)) => 3
    print(test) => [4]

    #최소값 삭제하지 않고 얻기
    print(heap[0])

    # 기존 리스트를 힙으로 변환
    test = [1,4,7,3]
    heapq.heapify(test)
    print(test) => [1,3,4,7]

    ## 최대 힙 활용
    # 각 값에 대한 우선 순위 구한 후, (우선 순위, 값) 구조의 튜플을 힙에 추가하거나 삭제하면 된다. 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 된다.

    data = [4,1,7,3,8,5]
    heap = []
    for num in data:
        heapq.heappush(heap,(-num,num)) # 우선순위, 값
    while heap:
        print(heapq.heappop(heap)[1])

```