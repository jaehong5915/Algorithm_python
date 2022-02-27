'''
게임을 만든 동준이
- n 개의 레벨, 각 레벨 클리어 시 점수 주어짐
- 쉬운 레벨이 어려운 레벨보다 점수를 많이 받는 경우 만들었음
입력)
n = 레벨의 수
    점수(n)
'''

n = int(input())
data =[]
for _ in range(n):
    data.append(int(input()))
a = data[0]
cnt = 0
rs =[]
i = 0
for i in range(n-2,-1,-1):
    if data[i] >= data[i+1]:
        cnt += data[i+1] - data[i] - 1
        data[i] = data[i+1]-1

print(abs(cnt))
    