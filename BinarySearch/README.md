# 이진 탐색

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