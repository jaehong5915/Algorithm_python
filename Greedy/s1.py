# 거스름돈
# 거스름돈 500원, 100원, 50원, 10원 -> 손님에게 거슬러 줘야 할 돈이 n원일 때 동전의 최소 개수는?
## 가장 큰 화폐단위부터 돈을 거슬러 주는 것.

n = 1260
count = 0

coin_type =[500, 100, 50, 10]

for coin in coin_type:
    count += n//coin #거스름돈을 동전으로 나눈 몫을 Count에 추가
    n %= coin

print(count)