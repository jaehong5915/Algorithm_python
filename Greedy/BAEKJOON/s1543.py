'''
어떤 단어가 몇번 등장하는지
abababa -> 'ababa' => 0번, 2번
중복 불가
'''
data = input()
chk = input()

cnt = 0
i = 0 
while i <= len(data) - len(chk): 
    if data[i: i+len(chk)] == chk:
        cnt += 1
        i += len(chk)
    else:
        i += 1
print(cnt)