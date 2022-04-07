# 백준 - 스택
# 시간초과 때문에 readline 써줘야 한다고 함 

import sys
input = sys.stdin.readline

N = int(input())

stack = []
for _ in range(N):
    
    C = list(input().split())
    
    if len(C) == 2:
        stack.append(int(C[1]))
    
    elif C[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif C[0] == 'size':
        print(len(stack))

    elif C[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif C[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()