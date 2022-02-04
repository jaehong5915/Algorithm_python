# Python

# **숫자형**

- **소수점 표현 방식**
    - a = 4.24E10  → 4.24 * 10^10/
- **8진수와 16진수**
    - 8진수 → 0o로 시작 →  a = 0o177
    - 16진수→ 0x로 시작 → a = 0x8ff

---

# 문자열

- **“Hello” , ‘Hello’, “””Hello”””, ‘’’Hello’’’**
- **이스케이프 코드**
    - \n → 문자열 안에서 줄을 바꿀 때 사용
    - \t → 문자열 사이에 탭 간격을 줄 때 사용
    - \\ → 문자 \를 그대로 표현할 때 사용
    - \’ → 작은따옴표를 그대로 표현할 때 사용
    - \” → 큰 따옴표를 그대로 표현할 때 사용
- **문자열 길이 구하기**
    - a = “Hello”   → len(a)
- **문자열 인덱싱과 슬라이싱**
    - a = Life is too short, You need Python
    - a[0] → ‘L’ ... a[3] → ‘e’   ... a[-1] → ‘n’
    - **a[시작 번호 : 끝 번호] → a[19:] ⇒ ‘You ~ Python’ // a[:17] ⇒ ‘Life is too short’**
    - a[19:-7] ⇒ a[19] ~ a[-8]
- **문자열 포매팅**
    - 숫자 & 문자 바로 대입 (숫자 : %d / 문자 : %s )
    
    ```python
    "I eat %d apples." %3     =>  "I eat 3  apples."
    
    "I eat %s apples." % "five" => "I eat five apples."
    ```
    
    - 2개 이상의 값 넣기
    
    ```python
    number = 10 
    day = "three"
    "I ate %d apples. so I was sick for %s days." %(number, day) =>
    "I ata 10 apples. so i was sick for three days."
    ```
    
    - **문자열 포맷 코드**
    
        **%s → 문자열** / %d → 정수 / %c → 문자 1개 / %f → 부동소수 / %o → 8진수 
    
        %x → 16진수 / %% → 문자 % 자체
    
    1. **정렬과 공백**
    - **%10s → 길이가 10인 문자열 공간에서 대입 값을 오른쪽 정렬 + 앞 공백으로 남겨둠**
    - **%-10s→ 왼쪽 정렬**
    1. 소수점 표현하기
    - “%0.4f” % 3.42134234 → ‘3.4213’ (소수점 네 번째 자리까지 표현
    - f**ormat 함수를 사용한 포매팅**
        - 숫자 바로 대입하기
            
            “I eat {0} apples”.format(3) → ‘I eat 3 apples.’
            
        - 문자열 바로 대입하기
            
            “I eat {0} apples”.format(”five”) → ‘I eat five apples’
            
        - 2개 이상 변수 대입
            
            ```python
            number = 10
            day = "three"
            "I eat {0} apples. so i was sick {1} days.". format(number, day)
            'I ate 10 apples. so i was sick three days.'
            ```
            
        - 정렬
            
            ```python
            "{0:<10}".format("hi")
            'hi          '
            :<10 표현식을 사용하면 치환되는 문자열을 왼쪽 정렬 + 문자열의 총 자릿수를 10으로 맞출 수 있음.
            
            "{0:>10}".foramt("hi")
            '          hi' 
            : < : > 화살표 방향에 따라 정렬 정할 수 있음.
            :^  -> 가운데 정렬
            "{0:=^10}.format("hi")" -> ====hi====
            ```
            
        - 소수점 표현하기
            
             y = 3.42134234 → “{0:0.4f}”.format(y) → 3.4213
            
        - { 또는 } 문자 표현하기
            
            “{{ and }}”.format()
            
        - **f 문자열 포매팅**
            
            age = 30
            
            f’나는 {age}살 입니다.’ 
            
            ---
            
- **문자열 관련 함수들**
    - 문자 개수 세기(count) → a.count(’b’)
    - 문자 위치 알려주기(find) → a.find(’b’) 처음으로 나온 위치 반환, 존재하지 않으면 -1 반환
    - 문자 위치 알려주기(index)→ a.index(’b’) 처음으로 나온 위치 반환, 존재하지 않으면 오류
    - 문자열 삽입(join) → “,”.join(’abc’) → a,b,c / 문자열 사이에 ‘,’ 삽입
        - 리스트, 튜플 사용 가능 → “,”.join([’a’, ’b’, ’c’, ’d’]) → a,b,c,d
    - 소문자를 대문자로(upper) → a.upper()
    - 대문자를 소문자로 바꾸기(lower) → a.lower()
    - 왼쪽 공백 지우기(lstrip) → a.lstrip() → ‘hi   ‘
    - 오른쪽 공백 지우기(rstrip)
    - 양쪽 공백 지우기(strip)
    - 문자열 바꾸기(replace) → a.replace(”Life”, “Your leg”) → Your leg is short
    - 문자열 나누기(split) → a.split(기준) → 없으면 공백 기준, [a, b, c, d]
    
    ---
    

# **리스트**

- e = [1, 2, [’Life’, ‘is’]] → 리스트 자체를 요솟값으로 가질 수 있음
- 비어 있는 리스트 a = list() 생성

---

- **리스트의 인덱싱과 슬라이싱**
    
    ```python
    a = [1,2,3,4,5]
    a[0] -> 1
    a[0:2] -> [1, 2]
    ```
    
- **리스트 연산 (같은 타입 가능 , del 함수)**
    
    ```python
    a = [1, 2, 3]
    b = [4, 5, 6]
    a+b -> [1,2,3,4,5,6]
    
    a = [1,2,3]
    a[2] = 4
    a -> [1,2,4]
    
    a = [1,2,3]
    del a[1] 
    a -> [1,3]
    
    a = [1,2,3,4,5]
    del a[2:]
    a -> [1,2]
    ```
    
- 리스트 관련 함수들
    
    ```python
    # append
    a = [1,2,3]
    a.append(4)
    a -> [1,2,3,4]
    a.append([5,6])
    a -> [1,2,3,4,[5,6]]
    -----------------------
    # sort
    a = [1,3,2,4,5]
    a.sort()
    a -> [1,2,3,4,5]
    -----------------------
    #reverse
    a = ['a', 'c', 'b']
    a.reverse()
    a -> ['b', 'c', 'a']
    -----------------------
    # index(x)
    # x의 위치 값을 돌려준다.
    a = [1,2,3]
    a.index(3) -> 2
    a.index(1) -> 0 
    -----------------------
    # insert(a,b) 
    # a번째 위치에 b를 삽입
    a = [1,2,3]
    a.insert(0,4)
    a -> [4,1,2,3]
    -----------------------
    # remove(x) 
    # 첫번째로 나오는 x 삭제
    a = [1,2,3,1,2,3]
    a.remove(3)
    a -> [1,2,1,2,3]
    -----------------------
    # pop()
    # 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
    a = [1,2,3]
    a.pop()
    a -> [1,2]
    a = [1,2,3]
    a.pop(1)
    a -> [1,3]
    -------------------------
    # count(x)
    # x가 몇개 있는지 개수를 표현
    a = [1,2,3,1]
    a.count(1)
    a -> 2
    ------------------------
    # extend([리스트])
    a = [1,2,3]
    a.extend([4,5]) == a+=[4,5]
    a -> [1,2,3,4,5]
    b = [6,7]
    a.extend(b)
    a -> [1,2,3,4,5,6,7]
    ```
    
    ---
    

# **튜플 , ()**

- 프로그램 실행되는 동안 값이 **변하지 않기를 바란다면** 튜플 사용, 반대 리스트 사용
- 튜플은 값의 생성, 삭제, 수정 불가

---

# **딕셔더리**

- dic = {’name’ : ‘jaehong’ , ‘phone’ : ‘010’ }
- Key와 Value를 한 쌍으로 갖는 자료형
    - Key : baseball / Value : 야구
    - Value에 리스트도 넣을 수 있음, Key는 고유 값 → 리스트 x, 튜플 o

---

- **딕셔너리 쌍 추가, 삭제하기**
    
    ```python
    # 딕셔너리 쌍 추가 
    a = {1 : 'p'}
    a[2] = 'b'
    a = {1: 'p', 2:'b'}
    a['name'] = 'pey'
    a = {1:'p', 2:'b', 'name':'pey'}
    a[3] = [1,2,3]
    a = {1:'p', 2:'b', 'name':'pey'}
    ----------------------------------
    # 딕셔너리 요소 삭제
    del a[1]
    a = {2:'b', 'name':'pey'}
    ```
    

---

- **딕셔너리 관련 함수**
    
    ```python
    # Key 리스트 만들기(keys)
     a = {'name' : 'pey', 'phone' : '010' } 
     a.keys()
    dict_keys(['name', 'phone'])
    ---------------------------------------
    # dict_key 객체를 리스트로 변환
    list(a.keys()) -> ['name', 'phone']
    ---------------------------------------
    # Value 리스트 만들기
    # values
    a.values()
    dict_values(['pey', '010'])
    ---------------------------------------
    # key : value 쌍 얻기(items)
    # items 함수는 key & value 튜플로 묵은 값을 dict_items 객체로 돌려준다.
    a.items()
    dict_items([('name','pey'), ('phone','010')])
    ---------------------------------------
    # key : value 모두 지우기 (clear)
    a.clear() 
    ---------------------------------------
    # key로 Value 얻기(get)
    a.get(key) -> value
    a = {'name':'pey', 'phone':'010'}
    a.get('name')  -> 'pey'
    # 없는 key -> return 'none'
    a.get('foo' , 'bar') -> bar
    ---------------------------------------
    # in (해당 key가 딕셔너리 안에 있는지 조사하기
    a = {'name':'pey', 'phone':'010'}
    'name'  in a -> True
    'email' in a -> False  
    ```
    

---

# 집합 자료형, set

```python
s1 = set()
s1 = set([1,2,3])
s1 -> {1, 2, 3}

s2 = set("hello")
s2 -> {'e', 'h', 'l', 'o'}
# 중복 허용 x , 순서가 없다. => 인덱싱 접근이 불가
# 인덱싱 접근 -> 리스트, 튜플로 변환 후 가능
s1 = set([1,2,3])

k1 = list(s1)
k1 -> [1,2,3] , k1[0] -> 1

a1 = tuple(s1)
a1 -> (1,2,3)
```

- 교집합, 합집합 , 차집합 구하기

```python
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합
s1 & s2 -> {4,5,6} == s1.intersection(s2)

#합집합 - 중복 값은 한개씩
s1 | s2 -> {1,2,3,4,5,6,7,8,9} == s1.union(s2)

#차집합
s1 - s2 -> {1,2,3}
s2 - s1 -> {7,8,9}
```

- 관련 함수

```python
# 값 1개 추가하기(add)
s1 = set([1,2,3])
s1.add(4)
s1 -> {1,2,3,4}

#값 여러개 추가하기(update)
s1 = set([1,2,3])
s1.update([4,5,6])
s1 -> {1,2,3,4,5,6}

#특정 값 제거하기(remove)
s1 = set([1,2,3])
s1.remove(2)
s1 -> {1,3}
```

---

# 조건문

- and, or, not
    - x or y → x와 y 둘중에 하나만 참이어도 참이다.
    - x and y → x와 y 모두 참이어야 참이다.
    - not x → x가 거짓이면 참이다.
    
    ```python
    money = 2000
    card = True
    if money >= 3000 or card:
    		print('택시')
    ```
    
- x in s, x not in s
    
    ```python
    1 in [1,2,3]     -> True
    1 not in [1,2,3] -> False
    ```
    
- 조건문에 아무 일도 하지 않게 설정
    
    > 주머니에 돈이 있으면 가만히 있고 돈이 없으면 카드를 꺼내라
    > 
    
    ```python
    poc = ['money', 'card']
    if 'money' in pocker:
    	pass
    else:
    	print('카드를 꺼내라')
    ```
    
- elif → 다중조건 판단
    
    ```python
    pocket =['paper','money']
    card = True
    if 'money' in pocker:
    	print('택시를 타고가라')
    elif card:
    	print('택시를 타고가라')
    else:
    	print('걸어가라')
    ```
    
- 조건부 표현식
    - 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
    - mes  = “suc” if score ≥ 60 else “fal”

---

# while문의 기본 구조

```python
while <조건문>:
	<수행문 1>
	<수행문 2>
========================
# 여러 선택지 중 하나 선택해서 입력받는 예제
prompt = ""
1. add
2. del
3. list
4. Quit
```

- while문의 맨 처음으로 돌아가기 (continue)

```python
a = 0
while a < 100:
	a += 1
	if(a%2 == 0):continue
		print(a)
```

---

# for문의 기본 구조

```python
for 변수 in 리스트( 또는 튜플, 문자열 ) :
		수행문 1
		수행문 2

# 다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a :
		print(first + last)
--> 3 ... 7 ... 11

```

- range 함수 : range(시작, 끝) → 시작 이상 끝 미만
    
    range(1,11) → 1이상 11미만
    
    ```python
    a = range(10) => 0부터 10미만의 숫자를 포함하는 range 객체 생성
    a --> range(0,10)
    ```
    
- 리스트 내포
    - **[표현식 for 항목 in 반복가능객체 if 조건몬]**
    - 리스트 안에 for 문을 포함하는 리스트 내포

```python
a = [1,2,3,4]
result = []
for num in a :
	result.append(num * 3)
print(result) -> 3, 6, 9, 12

## 리스트 내포 사용 
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

## 조건 사용
a = [1,2,3,4]
result = [num*3 for num in a if num%2 ==0 ]
```

---

# 함수

- 함수 안에서 사용하는 매개변수는 함수 밖의 변수와 무관

```python
def 함수명(매개변수) :
	 <수행문 1>
	 <수행문 2>
		....
```

- **매개변수와 인수**
    - 매개변수는 함수에 입력으로 전달된 값을 받는 변수
    - 인수는 함수를 호출할 때 전달하는 입력값

```python
def add(a,b):    # a, b는 매개변수
	return a+b

print(add(3,4)) # 3, 4 는 인수
```

- 매개변수 지정하여 호출 하기

```python
result = add(a=3, b=7)
print(result) --> 10
```

- **입력 값이 여러개**

```python
def 함수이름(*매개변수):
	<수행문 1>
```

- 키워드 파라미터 kwargs (**)

```python
def print_keywr(**kwargs):
	print(kwargs)

print_keywr(a=1) -> {'a' : 1}
print_keywr(name='foo' : age = 3} -> {'age':3,'name':'foo'}
```

- return의 또 다른 쓰임새

```python
def say_nick(nick):
	if nick == '바보':
		return
	print('내 별명은 %s 입니다.' %nick)
```

- 매개변수에 초깃값 미리 설정하기

```python
def say_myself(name, old, man=True):
	print('%s 입니다.'%name)
	print('%s살 입니다.'%old)
	if man:
		print('남자')
	else:
		print('여자')
```

- 함수 안에서 함수 밖의 변수를 변경하는 방법

```python
# return 사용하기
a = 1
def var(a):
		a += 1
		return a
a = var(a)
print(a)

## global 명령어 사용하기
a = 1
def var():
	global a
	a += 1
var()
print(a)
```

- lambda  매개변수1, 매개변수2, ...: 표현식

```python
add = lambda a,b : a+b
result = add(3,4)
print(result)

#def 
def add(a,b):
return a+b

result = add(3,4)
print(result)
```

---

# 입출력

- 입력받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장
    - list(map(int, input().split()))
    1. input으로 입력받은 문자열을 split()로 공백으로 나눈 리스트로 변경
    2. map을 이용 → 해당 리스트의 모든 원소에 int() 함수 적용
    3. 최종적으로 결과를 다시 list로 바꿈으로써 숫자 자료형으로 저장
        
        ```python
        #많은 수의 데이터를 입력 받을 때
        #정렬, 이진 탐색, 최단 경로 ,...
        
        import sys
        data = sys.stdin.readline().rstrip()
        ```
        
- 출력
    - 문자열 자료형끼리 연산 가능 → str(answer)

---

# 내장함수

- itertools
    - permutations → 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
    
    ```python
    from itertools import permutations
    data = ['a','b','c']
    result = list(permutations(data,3))
    #객체 초기화 이후에는 리스트로 변환하여 사용
    print(result)
    ==> [(a,b,c), (a,c,b) ,.... , (c,b,a)
    ```
    
    - combinations → 객체에서 r개의 데이터를 뽑아 순서 상관X, 중복 X
    
    ```python
    from itertools import combinations 
    data =['a','b','c']
    result = list(combinations(data,2))
    
    ==> [(a,b) , (a,c) , (b,c)
    ]
    ```
    
    - product → 객체에서 r개의 데이터를 뽑아 중복 허용
    
    ```python
    from itertools import product
    data = ['a','b','c']
    result2 = list(product(a,repeat=2))
    ==> [(a,a),(a,b),(a,c) ,....,(c,c)]
    ```
    
    - combinations_with_replacement
    
    ```python
    # 2개를 뽑는 모든 조합 (중복 허용)
    from itertools import combinations_with_replacement
    data = ['a','b','c']
    result = list(combinations_with_replacement(a,2))
    ==> [(a,a) , (a,b), (a,c) ,(b,b) ,...,(c,c)]
    ```
    
- **heapq (heapq.heappush() , heapq.heappop())**
    - 다익스트라 최단 경로 알고리즘을 포함해 우선순위 큐 기능 구현시 사용
    - 원소를 힙에 전부 넣었다가 빼면 크기순 정렬
    - 삽입 - .heappush() / 꺼냄 - .heappop()
    
    ```python
    # 힙 정렬 오름차순
    import heapq
    
    def heapsort(iter):
    	h = []
    	result = []
    	for value in iter:
    		heapq.heappush(h,value)
    	for i(_) in range(len(h)):
    		result.append(heapq.heappush(h))
    	return result
    
    result = heapsort([1,3,4,5,2,7])
    ==> [1,2,3,4,5,7]
    
    #내림차순
    import heapq
    
    def heapsort(iter):
    	h =[]
    	result = []
    	for value in iter:
    		heapq.heappush(h,-value) //-역순주고 다시 빼낼때 - 붙여서 빼냄
    	for _ in range(len(h)):
    		result.append(-heapq.heappush(h))
    	return result
    
    ```
    
- **bisect - bisect_left(), bisect_right()**
    - ‘정렬된 배열’에서 특정 원소를 찾아야 할 때 매우 효과적으로 사용
    - bisect_left() → 정렬 순서 유지, 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스
    - bisect_right() → 정렬 순서 유저, 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스
    
    ```python
    #[left, right] 사이 속한 인덱스 개수 반환 함수
    
    from bisect import bisect_left, bisect right
    
    def count_by_range(a, left_value, right_value):
    	right_index = bisect_right(a,right_value)
    	left_index = bisect_left(a,left_value)
    	return right_index - left_index
    
    a = [1,2,3,3,3,3,4,4,8,9]
    # 값이 4인 데이터 개수 출력 (left value = right value)
    print(count_by_range(a,4,4))
    # 값이 [-1, 3] 범위에 있는 데이터 개수 출력 
    print(count_by_range(a,-1,3))
    ```
    
- **collections - deque, Counter**
    - deque → 첫번째 원소 제거 : popleft(), 첫번째 원소 삽입 : appendleft()
    - counter → 원소 횟수 세기
    
    ```python
    from collections import deque, Counter
    
    #리스트 원소 삽입
    data = deque([2,3,4])
    data.appendleft(1)
    data.append(5)
    
    print(data) ==> deque([1,2,3,4,5])
    print(list(data)) ==> [1,2,3,4,5]
    
    #등장 횟수 세기
    counter = Counter(['red','blue','red','green','blue'])
    
    print(counter['blue']) ==> 2
    print(counter['red'])  ==> 2
    print(dict(counter))   ==> {'red':2, 'blue':2, 'green':1}
    ```
    
- **math - factorial(), sqrt(x), gcd(a,b), pi, e**
    - factorial(x) → x! 값 반환
    - sqrt(x) → x 제곱근 반환
    - gcd(a, b) → a와 b의 최대공약수 반환
    - pi → 파이 출력, e → 자연상수 e 출력
    
     
    
    ```python
    import math
    # factorial(x) 
    print(math.factorial(5)) ==> 5! (120)
    
    #sqrt(x)
    print(math.sqrt(7)) ==> 2.6457....
    
    #gcd(a,b)
    print(math.gcd(21,14)) ==> 7
    
    #pi, e
    print(math.pi) ==> 3.1415...
    print(math.e) ==> 2.718...
    ```