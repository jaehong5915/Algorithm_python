'''
110011 -> 0 or 1 로 통일하기
최소 수
'''
n = input()
cnt0 = 0
cnt1 = 0
if n[0] == '0':
    cnt1 +=1
else:
    cnt1 +=1
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i+1] == '1':
            cnt0 +=1
        else:
            cnt1 +=1
print(min(cnt0,cnt1))