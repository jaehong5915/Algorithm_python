'''
문자열 재정렬
알파벳 대문자 + 숫자로 구성된 문자열 입력
-> 모든 알파벳 오름차순 정렬 후 나머지 숫자 더한 값 출력
'''
from string import ascii_uppercase
n = input()
alpha = list(ascii_uppercase)
rs = []
sum = 0
for i in n:
    if i in alpha:
        rs.append(i)
    else:
        sum += int(i)
rs.sort()
rs.append(sum)
for i in rs:
    print(i, end='')