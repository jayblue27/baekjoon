# 시간초과 20~22
# def solution(numbers):
#     n = len(numbers)
#     answer = [-1] * n
        
#     max_val = max(numbers)
    
#     for i, num in enumerate(numbers):
#         for j in range(i,n):
#             if num >= max_val:
#                 break
#             if num < numbers[j]:
#                 answer[i] = numbers[j]
#                 break
        
#     return answer

# stack ?
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
        
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(i)
        
    return answer