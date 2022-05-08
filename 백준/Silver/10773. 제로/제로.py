# 백준 - 제로 
'''
틀린숫자 기입하면 
그 다음에 0을 외치고
앞에 숫자를 지운다.

0이 아니면 push
0을 만나면 pop
'''
import sys
input = sys.stdin.readline

#입력
N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if num != 0:
        stack.append(num)
    
    else:
        if stack:
            stack.pop()

print(sum(stack))