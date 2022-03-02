'''
설탕 배달
봉지 - 3, 5 kg
18kg 설탕- 5kg * 3 + 3kg * 1 ==> 4
정확하게 N 킬로그램 만들 수 없다면 -1 출력
점화식
N = 5a + 3b // min(a+b)
'''
n= int(input())
cnt = 0

while n >= 0 :
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1

    if n == 0 :
        cnt = (n+1)*cnt
        print(cnt)
        break
else:
    print(-1)