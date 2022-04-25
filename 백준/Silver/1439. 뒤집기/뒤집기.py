# 백준 - 뒤집기 - 그리디 
# 이진숫자 최소의 횟수로 바꿔서 한가지 수로 통일하기
# 출현 빈도가 적은 숫자의 갯수를 세면 된다.

# arr 입력
arr = input()

# 리스트 순회하면서 입력값이 바뀔때마다 stack에 쌓기
# stack pop 반복하기 싫은데 최소 2개의 원소가 있어야 진행이 되기 때문에 문제해결을 위해서 사용
stack = []
stack.append(arr[0])
for i in range(1,len(arr)):
    stack.append(arr[i])
    if stack[-2] == stack[-1]:
        stack.pop()

# 빈도가 작은 수의 갯수 출력        
# print(stack.count(num))

# stack에서 0과 1중 빈도가 적은애를 출력
if stack.count('0') > stack.count('1'):
    print(stack.count('1'))
else:
    print(stack.count('0'))