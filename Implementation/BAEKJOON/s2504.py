'''
## 스택을 활용
- LIFO '(([]))'
- 스택애 '(([' 가 있는 상태로 ']' 를 만나 스택의 TOP인 '[' 를 꺼내 쌍을 이루고
- 다음으로 ')' 를 만나 TOP인 '(' 를 꺼내 쌍을 이루기 때문에 올바른 괄호
- 닫는 괄호일 때, 직전 괄호와 쌍이 맞는 경우에만 곱하기 한다
괄호의 값
() - 2 , [] - 3, (x) - 2 * (x) , [x] - 3 * [x]
(xy) - (x) + (y)
ex) (()[[]])([]) ==>
()[[]] => 2 + 3*3 = 11 / (()[[]]) = 11 * 2 / ([]) = 3 * 2 ==> 22 + 6 = 28

( -> ] 
[ -> )
'''
from inspect import stack


data = list(input())
stack = []
answer = 0 #최종 합산 정수
tot = 1 #괄호에 따라 곱해줄 값
for i in range(len(data)):
    if data[i] == '(' :
        stack.append(data[i]) #stack에 괄호 append
        tot = tot * 2 # 괄호에 해당하는 정수 미리
    elif data[i] == '[':
        stack.append(data[i])
        tot = tot * 3 
    elif data[i] == ')':
        if not stack or stack[-1] == '[': #)일때 전 괄호가 [ or stack이 비었거나
            answer = 0 #잘못된 괄호
            break
        if data[i-1] == '(':
            answer += tot
        stack.pop() #괄호 짝이 맞으면 stack pop
        tot //= 2
    else: #data[i] == ']'
        if not stack or stack[-1] == '(':
            answer = 0 # 잘못된 괄호
            break
        if data[i-1] == '[':
            answer += tot
        stack.pop() #괄호 짝이 맞으면 stack pop
        tot //= 3

if stack: #스택 원소가 있으면
    print(0)
else: # 없으면
    print(answer)
