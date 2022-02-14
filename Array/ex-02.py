'''
성적이 낮은 순서로 학생 출력하기
N명의 학생, 학생의 이름 + 성적 입력 -> 성적이 낮은 순서대로 학생의 이름 출력
'''

n = int(input())
student =[]
data =[]
rs=[]
for i in range(n):
    data.append(input().split())

data = sorted(data, key=lambda student: student[1])

for i in range(len(data)):
    print(data[i][1], end=' ')