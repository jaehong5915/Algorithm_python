# 그룹 단어
## 중복단어 -> 연속되어야 그룹단어

n = int(input())
for j in range(n):
    data = input()
    for i in range(len(data)-1):
        
        if data[i] != data[i+1]:
            if data[i] in data[i+1:]:

                n -= 1
                print('n:::',n)
print(n)