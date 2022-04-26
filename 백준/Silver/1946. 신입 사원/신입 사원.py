# 백준 - 신입 사원 - 그리디, 정렬

# 신규사원 채용
# 1차 서류, 2차 면접
# 적어도 하나가 다른지원자보다 떨어지지 않는자만
# 1, 1 있으면 1명밖에 없는거지
# 선발할 수 있는 신입사원의 최대 인원수

# 1차 결과 기준으로 정렬 후
# 하나라도 뛰어난 경우 stack에 넣고 아닌경우 pop
# 남은 stack의 길이 출력

import sys
input = sys.stdin.readline

# 입력
T = int(input()) # test case
# T번 반복
for _ in range(T):
    applicants = int(input())
    rank = []
    for _ in range(applicants):
        first, second = map(int,input().split())
        rank.append((first, second))
    
    #정렬
    rank.sort(key=lambda x:x[1])
    rank.sort()

    #탐색 및 출력        
    stack = []
    stack.append(rank[0])
    for i in rank[1:]:
        stack.append(i)
        if stack[-1][0] < stack[-2][0] or stack[-1][1] < stack[-2][1]:
            continue
        else:
            stack.pop()

    print(len(stack))    