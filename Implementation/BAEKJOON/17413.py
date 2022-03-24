'''
단어 뒤집기2
'''

s = list((input()))

i = 0 # 탐색 인덱스
start = 0  # 알파벳 시작 인덱스 저장

while i < len(s):
    
    if s[i] == '<' :
        i += 1
        while s[i] != '>':
            i += 1
        i +=1
    elif s[i].isalnum() == True:
        start = i # 인덱스 저장
        while i < len(s) and s[i].isalnum() == True:
            i +=1
        temp = s[start : i]
        temp.reverse()
        s[start:i] = temp
    else:
        i +=1
print("".join(s))