'''
수가 주어지면 각 자리수 내림차순 정렬
'''
n = input()
rs=[]
for s in n:
    rs.append(s)
rs.sort(reverse=True)
for i in rs:
    print(i,end='')
