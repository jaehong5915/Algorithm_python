'''
스택 수열
# pop 해서 나온 값이 data[i] 같아야 함
'''
import sys
input = sys.stdin.readline


n = int(input())
chk = True
arr =[]
rs = []
pos = 1
for i in range(n):
    num = int(input())
    while pos <= num:
        arr.append(pos)
        rs.append('+')
        pos += 1
    if arr[-1] == num :
        # 같으면 Pop 빼내기
        arr.pop()
        rs.append('-')
    else:
        print('NO')
        chk = False
        break
if chk == True:
    for i in rs:
        print(i)
    # if i == data[i]:

