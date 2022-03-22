'''
에라토스테네스의 체
- 2부터 N까지 정수 적음
- 아직 지우지 않은 수 중 가장 작은수 - P (소수)
- P를 지우고, 아직 지우지 않은 P의 배수를 순서대로 지움
- 아직 모든 수를 지우지 않았다면 다시 2번단계로

입력)
N, K 주어짐
출력)
K 번째 주어진 수 출력
'''
n, k = map(int,input().split())
data = [False for _ in range(n+2)] # 빼낸 p 의 값 True
cnt = 0
for i in range(2,n+1):
    if data[i] == False: # n+1
        for j in range(i, n+1, i): # i의 배수 반복
            if data[j] == False:
                data[j] = True
                cnt += 1
                
                if cnt == k :
                    print(j)
                    break

