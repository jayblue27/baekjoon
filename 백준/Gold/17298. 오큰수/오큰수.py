# 입력
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# 미리 -1 선언하고 조건에 맞는 값이 있을 경우만 갱신
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)