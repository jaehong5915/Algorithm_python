# 자료구조
- 우선순위 큐(Priority Queue)
    - 우선순위가 가장 높은 데이터를 먼저 삭제하는 자료구조
    - 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인
```python
    # 스택 - 가장 나중에 삽입된 데이터 추출
    # 큐 - 가장 먼저 삽입된 데이터 추출
    # 우선순위 큐 - 우선순위가 가장 높은 데이터 추출
```
---

- heapq
    - 항상 루트노드 제거
        - 원소 제거 -> 가장 마지막 노드가 루트 노드에 위치한다.
    -모든 부모 노드는 자식 노드보다 값이 작거나 큰 이진트리 구조
    - 최소 힙 : 루드 노드 최소 (최솟값 제거), 최대 힙 : 최대값 제거
- heapq.heappush(heap,item): item을 heap에 추가
- heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴
- heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환

```python
    # 자바의 PriorityQueue 클래스 
    # 최소 힙 -> heapq 모듈을 통해 원소 추가, 삭제한 리스트
    # heappush(), heappop()
    # N개의 데이터를 넣었다가 모두 꺼내는 작업 O(NlogN)
    import heapq
    def heapsort(data):
        h = []
        result = []
        # 모든 원소를 차례대로 힙에 삽입
        for value in data:
            heapq.heappush(h,value)
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        for i in range(len(data)):
            result.append(heapq.heappop(data))
        return result
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    res = heapsort(arr)
    for i in range(n):
        print(res[i])
    # ----------------------------------------------------

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