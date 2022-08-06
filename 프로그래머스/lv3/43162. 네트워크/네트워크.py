from collections import deque

def solution(n, computers):
    
    computers = deque(computers)
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
