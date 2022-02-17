'''
럭키스트레이트
자릿수가 짝수인 문자열 -> 절반으로 나눈 왼쪽 자릿수 합 = 오른쪽 자릿수 합 : "LUCKY" 출력
'''
n = int(input())
data = []
left = 0
right = 0
for i in str(n):
    data.append(int(i))
half = round(len(data)/2)
for i in range(half):
    left += data[i]
for i in range(half, len(data)):
    right += data[i]
if left == right:
    print('LUCKY')
else:
    print('READY')