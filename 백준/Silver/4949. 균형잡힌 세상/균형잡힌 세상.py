# 백준 - 균형잡힌 세상
# 여는 괄호
brackets_o = ['(','['] 
# 닫는 괄호
brackets_c = [')',']']


while True:
    # 문자열 s 입력
    s = input()
    if s == '.':  # .만 있을경우 반복문 종료
        break
    
    stack = []   # stack 선언
    # 문자열 s 순환
    for i in s:
        # i가 여는 괄호일때
        # stack에 추가
        if i in brackets_o:
            stack.append(i)
        
        # stack이 비어있지 않은 상태에서
        if len(stack) != 0:
            # stack의 탑이 '('이고 ')' 와 만날경우 '('를 pop 한다.
            if stack[-1] == '(' and i == ')':
                stack.pop()
                continue
            # stack의 탑이 '['이고 ']' 와 만날경우 '['를 pop 한다.
            elif stack[-1] == '[' and i == ']':
                stack.pop()
                continue

        if i in brackets_c:
            stack.append(i)
            break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')