from collections import deque


def bfs(x, y, n):
    # 예외처리 6번 케이스
    if x == y:
        return 0
    
    q = deque()
    dist = [0] * (1000001)    
    
    q.append(x)
    
    while q:
        x = q.popleft()
        if 0 <= x + n <= 1000000 and dist[x + n] == 0:
            dist[x + n] = dist[x] + 1
            q.append(x + n)
        if 0 <= x * 2 <= 1000000 and dist[x * 2] == 0:
            dist[x * 2] = dist[x] + 1
            q.append(x * 2)
        if 0 <= x * 3 <= 1000000 and dist[x * 3] == 0:
            dist[x * 3] = dist[x] + 1
            q.append(x * 3)
            
    
    return dist[y] if dist[y] != 0 else -1


def solution(x, y, n):

    return bfs(x,y,n)
    