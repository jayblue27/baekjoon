#입력
N = int(input())

#테스트케이스 만큼 반복
for _ in range(N):
    # 괄호문자 입력
    tmp = input()
    # 스택 선언
    stack = []
    # 괄호문자 순환    
    for i in tmp:
        # 여는괄호이면 stack에 push
        if i == '(':
            stack.append('(')      
        # 닫는 괄호일 때  
        elif i == ')':
            # 스택이 비어있으면 No 출력 후 반복문 탈출
            if len(stack) == 0:
                print('NO')
                break
            # 아니라면 pop 실행    
            else:
                stack.pop()    
    # 문자열 순회 후       
    else:
        # 길이 남아있으면 NO 출력
        if len(stack) > 0:
            print('NO')          
        # 아무런 이상 없으면 YES 출력  
        else:
            print('YES')