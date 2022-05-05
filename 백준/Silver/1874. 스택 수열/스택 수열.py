# 백준 -  스택 수열
import sys

# 입력
# N 수열의 갯수
input = sys.stdin.readline
# 출력 push는 +로 / pop은 No로 / 불가능한 경우 No
N = int(input())
stack = []
answer = []
flag = 0
cur = 1

for _ in range(N):
    num = int(input())
    # 입력한 수를 만날 때 까지 오름차순으로 push
    while cur <= num:       
        stack.append(cur)  # push
        answer.append("+")
        cur += 1
    # stack의 TOP이 입력한 숫자와 같다면
    if stack[-1] == num:    
        stack.pop()         # pop
        answer.append("-")
    # stack의 TOP이 입력한 수와 다르면 flag 세우고
    else:                   
        flag = 1      

#출력                 
if flag == 0:
    for i in answer:
        print(i)
# flag가 있으면 NO 출력
else:
    print('NO')