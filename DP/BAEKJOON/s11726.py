'''
2 x n 타일링
2xN 직사각형을 1X2, 2x1 타일로 채우는 방법의 수를 구하여라
Dp - 점화식 , 이전값 활용
- 풀이를 해보며 규칙 찾기
An = An-1 + An+1 -- 점화식
'''
import sys
input = sys.stdin.readline

n = int(input())

rs = [0,1,2]

for i in range(3,n+1):
    rs.append((rs[i-1]+rs[i-2])%10007)

print(rs[n])