'''
쇠막대기
- ()(((()())(())()))(()) 
- ( : 막대기 시작 ) : 끝 , () 자르는 부분
# 자른 뒤 양 끝 pop ( )
'''
stack = []
ans = 0
n = list(input())

for i in range(len(n)):
    if n[i] == '(':
        stack.append(n[i])
    
    else: # ' ) '
        if n[i-1] == '(': #()
            stack.pop()
            ans += len(stack)
        else: # )) 끝 부분
            stack.pop()
            ans +=1
print(ans)
