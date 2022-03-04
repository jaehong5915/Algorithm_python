'''
연속합
입력받은 수열 중 연속된 임의의 수를 선택해서 합 -> max
'''
n = int(input())
data = list(map(int,input().split()))
# 더하다가 음수되면 이전까지 합 dp에 넣고 max(dp)
rs=[]
rs.append(data[0])
for i in range(len(data)-1):
    rs.append(max(rs[i]+data[i+1], data[i+1]))
print(max(rs))
# rs = []
# tot = 0
# for i in data:
#     tot += i
#     if tot < 0 :
#         rs.append(0)
#         tot = 0
#     else:
#         rs.append(tot)
# if max(rs) == 0:
#     print(max(data))
# else:
#     print(max(rs))