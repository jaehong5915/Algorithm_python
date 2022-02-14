# 정렬

- **선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬**

---

## 선택 정렬 - O(N^2)

- 매번 가장 작은 것을 선택하는 정렬
    1. 전체 중 가장 작은 데이터 선택 → 맨 앞 데이터와 바꾼다.
    2. 바꾼 데이터 (첫번째 데이터) 제외 데이터 중 가장 작은 데이터와 두번째 데이터 
    
    ```python
    # 선택 정렬
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    
    for i in range(len(array)):
    		min_index = i
    		for j in range(i+1, len(array)):
    				if array[min_index] > array[j]:
    						min_index = j
    		# 스와프
    		array[i], array[min_index] = array[min_index],array[i]
    
    print(array) ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
    
    - **스와프 : 특정 리스트의 두 변수의 위치를 변경하는 작업**
    
    ```python
    array = [5, 3]
    array[0], array[1] = array[1], array[0]
    
    print(array) --> [3, 5]
    ```
    

---

## 삽입 정렬 - O(N^2)

- 삽입 정렬은 특정한 데이터를 적절한 위치에 ‘삽입'하는 정렬
    1. 두 번째 데이터부터 시작 → 첫 번째 데이터의 좌&우에 삽입

```python
# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
		for j in range(i, 0, -1): # i부터 1까지 감소하며 반복
				if array[j] < array[j - 1]: #한 칸씩 왼쪽으로 이동
						array[j], array[j - 1] = array[j - 1], array[j]
				else: # 자기보다 작은 데이터 만나면 그 위치에서 멈춤
						break

print(array) ==> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 퀵 정렬 - O(NlogN) ~ O(N^2)

- 기준을 설정한 다음 큰 수와 작은 수를 교환 후 리스트를 반으로 나누는 방식
- **left(큰 수) 피벗(기준) right(작은 수)**
- 리스트에서 첫 번째 데이터를 피벗으로 정한다.

```python
# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
	if len(array) <= 1 :
			return array	
	pivot = array[0]
	tail = array[1:]
	left = [x for x in tail if pivot <= x]
	right = [x for x in tail if pivot > x]

	return quick_sort(left)+[pivot]+quick_sort(right)

print(quick_sort(array))

```

---

## 계수 정렬 - O(N+K) / N→ 데이터의 개수 , K → 최댓값

- **데이터의 범위가 제한 되어 정수 형태로 표현할 수 있을 때만 사용**
- 데이터의 크기가 많이 중복되어 있을수록 유리하다
    1. 별도의 리스트를 선언, 그 안에 정렬에 대한 정보 담는다.

```python
# 계수 정렬
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1) # 모든 범위 포함 리스트 선언

for i in range(len(array)):
		count[array[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for i in range(len(count)):
		for j in ragne(count[i]):
				print(i, end = ' ') # 등장 횟수만큼 인덱스 출력

==> 0,0,1,1,2,2,3,4,5,5,6,7,8,9,9
```