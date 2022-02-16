'''
무지의 먹방
1. food_time -> 순서대로 음식 섭취 1초당 원소 -1
2. food_time 원소 : 0 -> continue 다음 원소 -1
3. k - 방송 중단 시간 / 더 섭취할 음식 x -> '-1' 반환
19:00
s1) 인덱스로 접근 - 
## enumerate, itemgetter 개념정리 필요!!
'''

from operator import itemgetter


def solution(food_times, k):
    foods = []
    n = len(food_times)
    for i in range(n):
        foods.append((food_times[i], i+1))
    foods.sort()

    pretime =0 
    for i, food in enumerate(foods):
        diff = food[0] - pretime
        if diff != 0:
            spend = diff * n
            if spend <= k:
                k -= spend
                pretime = food[0]
            else:
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(1))
                return sublist[k][1]
        n -= 1
    return -1
print(solution([3,1,2],5))
