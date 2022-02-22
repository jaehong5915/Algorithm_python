'''
통나무 건너뛰기
- 인접한 통나무 높이차 = 난이도
출력)  난이도가 가장 낮은 통나무 배치의 난이도

입력)
t = 테스트케이스
n = 통나무 갯수
    - 통나무 높이
1) 오름차순 정렬

'''
t = int(input())
for _ in range(t):
    data =[]
    rs=[]
    n = int(input())
    data=list(map(int,input().split()))
    data = sorted(data)
    for i in range(2,n):
        rs.append(abs(data[i]-data[i-2]))
    print(max(rs))