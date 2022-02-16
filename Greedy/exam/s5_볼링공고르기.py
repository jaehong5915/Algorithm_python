'''
볼링공 고르기
공 갯수, 무게 범위 주어질 때 고를 수 있는 짝
'''

n, m = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0
for i in range(n):
    for j in range(i,n):
        if data[i] != data[j]:
            print(data[i],data[j])
            cnt +=1
print(cnt)