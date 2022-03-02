'''
가방에 물건을 담는다.
물건은 가치와 무게가 정해져있음
최대 5키로
무게/가치
(1/30), (2/20), (3/40), (4/10) -- 가방에 넣을 수 있는 최대 가치는?
'''
n, k = map(int,input().split())
wei=[]
val=[]
for _ in range(n):
    w, v = map(int,input().split()) 
    wei.append(w)
    val.append(v)
