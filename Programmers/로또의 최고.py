'''
모르는 번호 '0'
rs = [최고, 최저]
'''
data = list(map(int,input().split()))
win_data = list(map(int,input().split()))
def solution(lottos, win_nums):
    cnt = 0
    z_cnt = 0
    rs = []
    for i in lottos:
        if i == 0 :
            z_cnt += 1
        for j in win_nums:
            if i == j:
                cnt +=1
    rs.append(cnt+z_cnt)
    rs.append(cnt)
    answer = []
    for i in rs:
        if i == 6:
            answer.append(1)
        elif i == 5:
            answer.append(2)
        elif i == 4:
            answer.append(3)
        elif i == 3:
            answer.append(4)
        elif i == 2:
            answer.append(5)
        else:
            answer.append(6)
    return answer

print(solution(data,win_data))