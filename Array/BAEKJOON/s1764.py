'''
듣보잡
# '''
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
h = set()
s = set()
for _ in range(n):
    h.add(input().strip())
for _ in range(m):
    s.add(input().strip())
rs = sorted(list(h&s))
print(len(rs))
for i in rs:
    print(i)

# print(len(rs))
# for i in rs:
#     print(i)