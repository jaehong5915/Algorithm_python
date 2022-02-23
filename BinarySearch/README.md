# 이진 탐색
```
# 대표적 유형
~~ 길이를 구하여라
start = 가장 짧은길이 Ex)1 , end = max(data)
while start <= end:
	mid = ( start + end )//2
	cnt = 0
	for i in data:
		cnt += i or cnt += i // mid (분할)
		if cnt >= N (분기점 EX)기준점)
			start = mid + 1
		else:
			end = mid - 1
print(end)
```
- 두 리스트 크기 비교시
	- 중간값, 타겟 활용
	- data[mid] < target[m] -> target[m] 값 미만은 모두 data[mid] 보다 작음
	- 해당 인덱스 값을 cnt 에 저장, 작은 원소 갯수 출력 
-**bisect**
    ```
    bisect.bisect(a,x) : a에 있는 x의 기존 항목 뒤에 오는 삽입 위치 반환
    ex) a = [8, 1, 7, 3, 1] b = [1, 3, 6]
    print(bisect.bisect(b,a[i])) -> a[i]가 b에 들어갈 우측 인덱스 반환
    bisect_left(literable, value): 왼쪽 인덱스 구하기 (초과범위)
    bisect_right(literable,value): 오른쪽 인덱스 구하기 (미만범위)
    ex)
    import bisect
    result = []
    for score in [33,99,77,70,89,90,100]:
        pos = ***bisect.bisect***([60,70,80,90], score)
        grade = 'FDCBA'[pos]
        result.append(grade)
    print(result) => ['F','A','C','C','B','A','A']

    #bisect.insort - 정렬된 위치에 해당 항목 삽입
    a = [60,70,80,90]
    bisect.insort(a,85)
    a -> [60,70,80,85,90]
    ```
---

## 순차 탐색 - 데이터 정렬 여부 x, 앞 데이터부터 하나씩

- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

```python
# 데이터 하나씩 순차적 방문
def search(n, target, array):
	#각 원소를 하나씩 확인
	for i in range(n):
		if array[i] == target:
			return i + 1 # 현재 위치 반환 idx 값이기에 +1

input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input+data[1] # 찾고자 하는 문자열

array = input().split()

```

---

## 이진 탐색 - 반으로 쪼개면서 탐색하기 (중간값 위치 기준)

- 리스트 안에 찾으려는 데이터와 중간점 위치에 있는 데이터 반복적으로 비교
- 탐색 범위가 2,000만을 넘어가면 이진 탐색으로 문제에 접근해보기

```python
# 재귀함수로 구현한 이진 탐색
def search(array, target, start, end):
	if start > end :
			return None
	mid = (start + end) // 2 --> 중간값, 찾은 경우 중간점 인덱스 반환 
	
	if array[mid] == target:
		return mid
	
# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
	elif array[mid] > target:
		return search(array,target,start, mid-1)
# 중간점의 값보다 찾고자 하는 값이 큰 경우 왼쪽 확인		
  else:
		return search(array, target, start ,mid +1)

n , target = list(map(int,input().split())) # 원소의 개수 N, 찾을 문자열 target

# 전체 원소 입력받기
array = list(map(int,input().split())

# 이진 탐색 수행 결과 출력
rs = search(array, target, 0, n-1)
if rs == None:
		print('원소 X')
else:
	print(rs + 1)

## 반복문으로 구현한 이진 탐색

def search(array, target, start, end):
	while start <= end :
		mid = (start+end) //2 # 중간점 인덱스
		if array[mid] == target:
			return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif array[mid] > target:
			end  = mid - 1
		# 중간점의 값보다 찾고자 하는 값이 큰 경우 왼쪽 확인		
	  else:
			start = mid + 1

return None

n , target = list(map(int,input().split())) # 원소의 개수 N, 찾을 문자열 target

# 전체 원소 입력받기
array = list(map(int,input().split())

# 이진 탐색 수행 결과 출력
rs = search(array, target, 0, n-1)
if rs == None:
		print('원소 X')
else:
	print(rs + 1)
```