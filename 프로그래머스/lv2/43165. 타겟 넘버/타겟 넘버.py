# DFS - 재귀 함수 - 0.51~ 390.94ms
def solution(numbers, target):
    n = len(numbers) #길이
    answer = 0
    def dfs(idx, result):  # dfs 함수
        if idx == n:       # idx가 끝에 도달하고
            if result == target:  # 값이 target에 도착하면
                nonlocal answer  
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer


# from collections import deque
# # BFS with deque - 0.55ms ~ 1187.45ms
# def solution(numbers, target):
#     answer = 0 
#     queue = deque()  # queue 생성
#     n = len(numbers) # numbers 길이
    
#     queue.append([ numbers[0],0]) # +number, 0번 index
#     queue.append([-numbers[0],0]) # -number, 0번 index
    
#     while queue:         
#         temp, idx = queue.popleft()
#         idx += 1 
#         # 모든 number 순환 전까지는 모든 경우의 수 만들어서 append
#         if idx < n: 
#             queue.append([temp+numbers[idx], idx])
#             queue.append([temp-numbers[idx], idx])
#         # temp 값이 target 값이면 count 1개씩 올리기
#         else:
#             if temp == target:
#                 answer += 1
#     return answer
