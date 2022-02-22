'''
신입 사원
입력)
t = 테스트케이스
n = 회사원 수
    - 순위!!! a, b

변수 cnt 

'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = [list(map(int,input().strip().split())) for _ in range(n)]
    cnt = 1
    data.sort()
    h = data[0][1]
    for i in range(1,n):
        if h > data[i][1] :
            h = data[i][1]
            cnt +=1
    print(cnt)