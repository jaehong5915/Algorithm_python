'''
용돈 관리

'''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data =[]
for _ in range(n):
    data.append(int(input()))
start = 1
end = sum(data)
# end = sum(data)
# cnt = 0
mon = 0
while start <= end:
    mid = (start+end)//2 #인출 금액
    mon = mid # 가진 돈
    cnt = 1
    for i in data:
        if mon < i : # 돈 부족하면 인출
            mon = mid
            cnt += 1
        mon -= i  
        # 돈 부족하지 않으면 그대로 생활
        # 남은거 다시 넣고 k원 인출
            
# m번보다 더 많이 인출하거나 인출 금액이 적은 경우 (인출금이 적기에 mid 를 높여아함)
    if cnt > m or mid < max(data):
        start = mid + 1
    else:
        end = mid - 1
        k = mid
print(k)