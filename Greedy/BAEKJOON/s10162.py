# 전자레인지 5분 , 1분 , 10초
# 최소버튼
t = int(input())
time_type=[300, 60, 10]
while t%10 == 0:
    for time in time_type:
        count = 0
        count += t//time
        t %= time        
        print(count, end=' ')       
    if t == 0:
        break
else:
    print(-1)
    
