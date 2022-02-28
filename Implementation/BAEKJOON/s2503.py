'''
숫자 야구
- 숫자가 동일 자리 - 스트라이크, 존재하나 다른자리 - 볼
입력)
n - 물음 갯수
세자리 수, 스트라이크, 볼

순열 + 인덱스로 풀이
'''
from itertools import permutations
n = int(input())
num = list(permutations([1,2,3,4,5,6,7,8,9],3)) #3자리 조합
for _ in range(n):
    data, strike, ball = map(int,input().split())
    data = list(str(data))
    cnt = 0

    for i in range(len(num)):
        scnt = 0
        bcnt = 0
        i -= cnt

        for j in range(3): # 비교
            data[j] = int(data[j])
            if data[j] in num[i]:
                if j == num[i].index(data[j]):
                    scnt += 1
                else:
                    bcnt += 1
        
        if scnt != strike or bcnt != ball :
            num.remove(num[i])
            cnt += 1
print(len(num))
