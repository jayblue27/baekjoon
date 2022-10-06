# 얼음 얼려먹기 처럼 풀면 되겠다. 
# 서로 연결되어 있는 요소가 몇 개인지 구하는 문제

# DFS- 재귀횟수 초과 df를 너무 많이 썼나? -> 재귀 제한 100만으로 늘려도 안된다. 
# import sys
# sys.setrecursionlimit(1000000)

# def solution(n, computers):
    
#     def dfs(j,i):
#         if j <= -1 or j>= n or i <= -1 or i >=n:
#             return False
    
#         nonlocal computers
#         if computers[j][i] == 1: # 해당위치에 컴퓨터가 있는경우
#             computers[j][i] == 0 # 방문처리
#             # 재귀호출 
#             dfs(j-1, i)
#             dfs(j+1, i)
#             dfs(j, i-1)
#             dfs(j, i+1)
#             return True
#         return False

#     n_network = 0
#     for j in range(n):
#         for i in range(n):
#             if dfs(j,i) == True:
#                 n_network += 1
                
#     return n_network



from collections import deque
def solution(n, computers):
    # computers = deque(computers)
    network = 0
    global visited
    visited = [False] * n
    
    for k in range(n):
        if BFS(n, computers, k, visited)==True:
            network += 1
        
    return network

def BFS(n, computers, k, visited):
    
    if visited[k]==True:
        return False
    
    queue = deque([computers[k]])
    visited[k] = True
    
    while len(queue)>0:
        node = queue.popleft()
        for i in range(n):
            if i!=k and node[i]==1:
                if visited[i]==False:
                    visited[i] = True
                    queue.append(computers[i])
                    
    return True
