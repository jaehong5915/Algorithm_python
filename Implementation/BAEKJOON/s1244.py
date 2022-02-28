'''
스위치 켜고 끄기

1 : 스위치 켜짐 , 0 : 꺼짐
학생들은 자신의 성별, 받은 수에 따라 스위치 조작
남 - 스위치 번호가 받은 수의 배수, - 상태 바꿈 (On -> off)
ex) n = 3 -> 스위치 3, 6 상태 변경
여 - 받은 수와 같은 번호 스위치를 중심, 좌우가 대칭이며 가장 많은 스위치를 포함 하는 구간
    속한 스위치 상태 변경
ex) n = 3 -> 1 ~ 5 번 스위치 

입력)
스위치 처음 상태, 각 학생의 성별, 수

출력)
스위치 마지막 상태 출력
'''
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
st_n = int(input())
for _ in range(st_n):
    st = list(map(int,input().split()))
    if st[0] == 1:
        for i in range(st[1]-1,len(data),st[1]):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0
    else:
        if data[st[1]-1] == 0:
            data[st[1]-1] = 1
        else:
            data[st[1]-1] = 0
        l = st[1] - 2
        r = st[1]
        while l >= 0 and r < n and data[l] == data[r]:
            if data[l] == 0:
                data[l] = 1
                data[r] = 1
            elif data[l] == 1:
                data[l] = 0
                data[r] = 0
            l -= 1
            r += 1
            if l < 0 or r >= n:
                break

for i in range(len(data)):
    if i%20 == 0 and i != 0:
        print()
    print(data[i],end=' ')
