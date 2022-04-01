'''
스택
push X : 정수 X를 스택에 넣음
pop : 가장 위 정수 빼고, 출력 없으면 -1
size : 스택 정수 개수 출력
empty: 스택 비면 1, 아니면 0 출력
top : 가장 위 정수 출력, 없으면 -1
'''
import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    order = input()
    if 'push' in order:
        a1 = order.split()
        data.append(int(a1[1]))
    # push 일 때 넣기
    else:
        if 'pop' in order:
            if len(data) > 0:
                print(data.pop())
            else:
                print(-1)
        elif 'size' in order:
            print(len(data))
        elif 'empty' in order:
            if len(data) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(data) > 0:
                print(data[-1])
            else:
                print(-1)