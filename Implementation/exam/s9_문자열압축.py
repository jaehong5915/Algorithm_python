'''
문자열 압축
1) N개 단위로 문자열을 자른다.
    - 
# 1개, 2개, 3개, ..., n개
# rs.append(cnt) -> min(rs)
# 첫원소도 안되면 False

'''
def solution(s):
    # 최소값을 찾아야하기에 answer가 가질 수 있는 최대 -> 문자열 길이
    answer = len(s)
    # i -> 압축 단위 1부터 ~ 문자열 길이 절반까지
    # 절반보다 압축길이가 커지면 압축이 아님
    for i in range(1, int(len(s)/2 +1)):
        pos = 0 # 지금 어느 위치에서 문자를 처리하는지 표현 변수
        length = len(s) 
        # 진행이 문자열 끝까지 갈 때 까지 진행 (pos+i == len)
        while pos + i <= len(s):
            # i = 1, i=2 ,.. 단위길이 만큼, pos 도 진행
            unit = s[pos:pos+i]
            pos += i
            cnt = 0
            # unit == 'ab' 이면 다음 문자도 ab인지 확인해야함 -> while
            while pos + i <= len(s):
                if unit == s[pos:pos+i]:
                    cnt += 1 #또 같은걸 만나면 +1
                    pos += i # pos 진행
                else:
                    break
            if cnt > 0 :
                print('length::',length)
                print('11',i*cnt)
                length -= i *cnt #i는 몇개씩 묶었는지, cnt 반복 횟수
                print('length22',length)
                #반복 횟수 10a => len(a) + 2
                        #   9a -> +1
                if cnt < 9 :
                    length += 1
                elif cnt < 99 :
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4
        print('ans:::',answer)
        print('len:::',length)
        answer = min(answer, length)
    return answer

print(solution('abcabcdede'))