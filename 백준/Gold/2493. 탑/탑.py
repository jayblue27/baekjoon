n = int(input())
tower = list(map(int, input().split()))

stack = [] # stack 선언
ans = [0] * n # 답지
 
for i in range(n):
    while stack:
        if stack[-1][1] > tower[i]:
            ans[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tower[i]])
 
print(*ans)