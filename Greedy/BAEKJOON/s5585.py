# 1000엔 주고 받을 거스름돈 (최소)
## 동전은 -> 500엔 / 100엔/ 50엔/ 10엔/ 5엔/ 1엔

N = int(input())
cha = 1000 - N
coin_type=[500, 100, 50 , 10, 5, 1]
count = 0
for coin in coin_type:
    if cha % coin >=0:
        count += cha//coin
        cha %= coin
print(count)