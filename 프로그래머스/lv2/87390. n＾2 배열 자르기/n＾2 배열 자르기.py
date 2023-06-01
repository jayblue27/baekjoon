# 1 2 3 
# 2 2 3
# 3 3 3 

# n = 3
# 0 1 2 3 4 5 6 7 8
# 몫 + 1
# 1 1 1 2 2 2 3 3 3
# 나머지 + 1
# 1 2 3 1 2 3 1 2 3 

# 1 2 3 2 2 3 3 3 3 

def solution(n, left, right):
    answer = []
    for p in range(left, right+1):
        # temp = []
        # temp.append(p//n)
        # temp.append(p%n)
        # answer.append(max(temp) + 1)
        answer.append(max(p//n + 1, p%n + 1) )
    return answer