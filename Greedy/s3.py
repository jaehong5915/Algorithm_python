'''
숫자 카드 게임
- 행 중에 최소 값 뽑기 
- 뽑은 값 중 가장 큰 값 
'''
n, m = map(int,input().split())
data = []
rs =[]
for _ in range(n):
    data=list(map(int,input().split()))
    rs.append(min(data))
print(max(rs))
    
# n,m = map(int, input().split())

# result = []
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result.append(min_value)
# print(max(result))