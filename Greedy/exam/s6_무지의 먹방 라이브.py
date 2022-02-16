'''
무지의 먹방
1. food_time -> 순서대로 음식 섭취 1초당 원소 -1
2. food_time 원소 : 0 -> continue 다음 원소 -1
3. k - 방송 중단 시간 / 더 섭취할 음식 x -> '-1' 반환
19:00
s1) 인덱스로 접근 - 
'''


# food_times = [3,1,2]
# k = 5
# j = 0
def solution(food_times, k):
    answer = 0
    i =0
    while i < 5:
        if food_times[answer] == 0:
            answer +=1
        else:
            food_times[answer] -= 1
            i +=1
            answer +=1
            if answer >= 3:
                answer -= 3

        if i == k:
            break
    
    return answer+1
print(solution([3,1,2],5))
