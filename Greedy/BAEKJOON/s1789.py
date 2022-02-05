# 수들의 합
## 서로 다른 N개의 자연수의 합 S , 자연수 N의 최댓값?
### 최댓값 -> 가장 작은 수부터 
s = int(input())
cnt = 0
tot = 0 
while True:
    cnt += 1
    tot += cnt
    if(tot == s):
        print(cnt)
        break
    if(tot >= s):
        print(cnt-1)
        break    
