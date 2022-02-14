'''
위에서 아래로
수열을 내림차순으로 정렬하는 프로그램
'''

n = int(input())
data =[]
for i in range(n):
    data.append(int(input()))
data.sort(reverse=True)
for i in range(len(data)):
    print(data[i], end=' ')