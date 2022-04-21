'''
방 번호


다시 풀어보기 꼭
'''


n = input()
rs = {'0':0, '1':0, '2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
for i in range(len(n)):
    if n[i] in ['6','9']:
        rs['6'] += 1
    else:
        rs[n[i]] += 1
if rs['6'] %2 == 0:
    rs['6'] = rs['6']//2
else:
    rs['6'] = rs['6']//2 + 1
print(max(rs.values()))