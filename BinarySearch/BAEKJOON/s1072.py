'''
게임
- 형택이의 승률이 변하려면 몇판을 더 해야 하는가
    - 앞으로 승리만 함
입력)
x = 게임 횟수 , y = 이긴 게임
z = int((x/y)*100) = 확률
target : 승률
z = 100 -> return -1
start , end 승률?
'''
x, y = map(int,input().split())
z = (y*100)//x
if z >= 99:
    print(-1)
else:
    cnt = 0
    start = 1 
    end = x
    while start <= end:
        mid = (start+end)//2
        if (y+mid)*100//(x+mid) <= z:
            start = mid + 1
        else:
            cnt = mid
            end = mid - 1
    print(cnt)
    
    