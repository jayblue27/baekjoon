import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

q = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            q.append((i,t))
    arr.append(temp)

mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while q:
        x, y = q.popleft()
        for k in range(8):
            dx = x + mx[k]
            dy = y + my[k]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0:
                    q.append((dx,dy))
                    arr[dx][dy] = arr[x][y] + 1
    return


bfs()
safe_dist = 0
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist, arr[i][j])

print(safe_dist - 1)