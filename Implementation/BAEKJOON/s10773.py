'''
제로
수를 잘못부르면 '0' - pop
입력)
정수 k, 4개의 줄에 정수 
정수 = 0 -> 지움 
'''
import sys
input = sys.stdin.readline

k = int(input())
data = []
for _ in range(k):
    num = int(input())
    if num == 0:
        data.pop()
    else:
        data.append(num)
print(sum(data))