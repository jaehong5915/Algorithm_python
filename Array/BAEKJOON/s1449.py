'''
수리공 항승
N: 갯수, L: 테이프 길이 , 위치
1. 파이프 물 새는 위치 오름차순 정렬
2. last = 테이프 끝지점 
3. 데이터가 정수인것에 주목하여 풀이
'''
n,l = map(int,input().split())
data=list(map(int,input().split()))
data.sort()
stat = data[0]
end = data[0] + l - 0.5
cnt =1
for i in data:
    if end > i:
        continue
    else:
        cnt+=1
        end = i+l-0.5
print(cnt)