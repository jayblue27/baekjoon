'''
문자열 괄호가 주어지고
제대로 열리고 닫혔으면 true
아니면 false 반환하라 

여는 괄호 append
닫는 괄호 만날경우 pop 

s가 있으면 false
s가 비어있으면 true

(예외처리) 처음부터 닫히는게 들어오면 false

'''
def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
            
        else:
            if not stack:
                return False
            else:
                stack.pop()
                
    return stack==[]
    
    
