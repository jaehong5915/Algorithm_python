'''
쉬운 계단 수
계단 수 = 인접한 모든 자리의 차가 1인 수

입력)
N , 길이가 n인 계단 수가 몇개 있는지?
'''
n = int(input())
dp = [0, 9] #dp -> 길이가 N인 계단 수 

for i in range(10**(n-1),10**n-1):
    print(i)