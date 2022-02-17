'''
문자열 압축
1) N개 단위로 문자열을 자른다.
    - 
# 1개, 2개, 3개, ..., n개
# rs.append(cnt) -> min(rs)
# 첫원소도 안되면 False

'''
def solution(s):
    answer = len(s)
    for i in range(1, int(len(s)/2 +1)):
        pos = 0
        length = len(s)
        while pos + i <= len(s):
            unit = s[pos:pos+i]
            pos += i
            cnt = 0
            while pos + i <= len(s):
                if unit == s[pos:pos+i]:
                    cnt += 1
                    pos += i
                else:
                    break
            if cnt > 0 :
                length -= i *cnt
                if cnt < 9 :
                    length += 1
                elif cnt < 99 :
                    length += 2
                elif cnt < 999:
                    length += 3
                else:
                    length += 4
        answer = min(answer, length)
    return answer

print(solution('abcabcdede'))