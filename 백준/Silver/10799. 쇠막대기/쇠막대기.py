# 백준 - 쇠막대기
bar = list(input())
ans = 0
stack = []

# 쇠막대기 순환
for i in range(len(bar)):
    # 여는괄호는 append
    if bar[i] == '(':
        stack.append('(')
    
    # 닫는 괄호 나올때
    else:
        if bar[i-1] == '(': 
            stack.pop()
            ans += len(stack)

        else:
            stack.pop() 
            ans += 1
# 출력
print(ans)