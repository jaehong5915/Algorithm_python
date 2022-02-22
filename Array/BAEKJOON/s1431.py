'''
시리얼 번호
- a,b 길이가 다르면, 짧은것이 먼저 온다.
- 길이가 같으면 모든 자리수의 합이 작은 것이 먼저 온다(숫자만)
- 사전순으로 비교 -> 숫자가 알파벳보다 사전순으로 작다.
입력)
- 기타 개수 N <= 50
    - 시리얼번호
'''
n = int(input())
seri = []
for _ in range(n):
    seri.append(input())

seri = sorted(seri, key=lambda x:len(x))
sum =0 
for i in seri:
    for j in range(len(i)):
        if type(i[j]) == 'int':
            sum += i[j]
            i[j] = sum
    print(i)