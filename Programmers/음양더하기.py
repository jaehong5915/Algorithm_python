'''
'''
data = list(map(int,input().split()))
sign = list(map(int,input().split()))

def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
        
    answer = sum(absolutes)
    return answer

print(solution(data,sign))