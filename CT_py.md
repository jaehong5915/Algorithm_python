# 코딩테스트.py

```python
# 아스키코드를 활용해 알파벳 출력
# 소문자
for i in range(97,123):
	print(chr(i),end='')
-> abcdef,,,z

# 대문자
for i in range(65,91):
	print(chr(i), end='')
-> ABCDEF,,,Z

# 숫자 반환
ord('바꿀 문자')
ord('a') -> 65

## index 문제 -> index 리스트 생성
a = list(map(int,input().split())))
a_idx = list(range(n))


## enumerate( , 시작값) 함수
for i, name in enumerate(l, 1):
	print(i, name) 
--> 1 name[0]  2 name[1]  3 name[2]

## LIST 내포 -> [식 for 변수 이름 in 개체]
s = [ i**2 for i in range(5)]
print(s) -> [0, 1, 4, 9, 16]

## if ~ is , if ~ is not

for i in range(len(alpha)):
	# 타입이 str 이면 ~ if type(a) is str:
    if type(alpha[i]) is str:
        alpha[i] = -1
```