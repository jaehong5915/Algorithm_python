'''
피보나치 함수

fibo(0) , fibo(1) 호출 수 출력
'''

def fibo(x):
    global zero
    global one
    if x == 0:
        zero += 1
        # cnt.append(zero)
        return 0
    if x == 1:
        one += 1
        return 1
    
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

t = int(input())
for _ in range(t):
    zero, one =0, 0
    n = int(input())
    d = [0] * (n+1)
    fibo(n)        
    print(zero, one)