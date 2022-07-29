# 입력
strings = input()

# 풀이
result = '' # 결과값 변수
stack = []  # 스택선언


for c in strings:
    if c.isalpha():
        result += c
        # print('A',result, stack)
    else:
        if c == '(':
            stack.append(c)
            # print('B',result, stack)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result+=stack.pop()
                # print('C',result, stack)
            stack.append(c)
            # print('D',result, stack)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
                # print('E',result, stack)
            stack.append(c)
            # print('F',result, stack)
        elif c == ')':
            while stack and stack[-1] != '(':
                result+=stack.pop()
                # print('G',result, stack)
            stack.pop()
            # print('H',result, stack)

while stack:
    result += stack.pop()

print(result)