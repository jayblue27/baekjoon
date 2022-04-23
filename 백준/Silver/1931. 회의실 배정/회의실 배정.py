#입력
# 회의수
N = int(input())
# 회의 시작/종료시간 arr
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))

# 시작시간으로 정렬 후, 종료시간으로 정렬
arr.sort(key = lambda x:x[0])
arr.sort(key = lambda x:x[1])

# stack 이용
stack = []
stack.append(arr[0])

for i in range(1, (len(arr))):
    stack.append(arr[i])
    # 직전스택의 마지막 회의종료 시간이
    # 마지막 스택의 회의시작시간보다 늦으면
    # 해당 회의는 못하는 걸로
    if stack[-2][1] > stack[-1][0]:
        stack.pop()

# stack에 남아있는 회의수 출력   
print(len(stack))