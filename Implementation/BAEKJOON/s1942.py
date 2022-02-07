# 요일 구하기
## 일 더해서 구하기 (월로 넘어가는 것 신경 쓰지 말기)
x,y = list(map(int,input().split()))
day = 0
week=['MON','TUE','WED','THU','FRI','SAT','SUN']
data=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range (x-1):
    day += data[i]
print(week[(day + y)%7-1])
    