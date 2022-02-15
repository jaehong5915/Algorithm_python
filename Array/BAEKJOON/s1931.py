'''
***다시 풀어보기 02/15***
회의실 배정
1. 회의 수, 시작 시간, 끝나는 시간
2. 최대 회의 가능 횟수 출력
+ 회의 시작과 끝 같으면 -> 시작하자마자 끝나는 회의
+ 가장 이른시간부터 체크 -> 긴 회의 제외하기 ex) 2- 12
sol) 시작시간으로 오름차순 -> 끝나는 시간으로 오름차순
    ->> (2,2) (1,2) 의 경우 cnt = 1 출력 / 따라서 (1,2) (2,2) 양상이 보이게 2번 정렬
'''
n = int(input())
data = []
rs = []
for i in range(n):
    a,b = map(int,input().split())
    data.append([a,b])
data = sorted(data,key=lambda x:x[0])
data = sorted(data, key=lambda a:a[1])
last =0
cnt =0
for i,j in data:
    if i >= last:
        cnt+=1
        last = j
print(cnt)