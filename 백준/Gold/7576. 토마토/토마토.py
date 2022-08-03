# bfs는 queue를 사용한다. 
from collections import deque
queue = deque([])

#입력
M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]

#방향 리스트
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
res = 0

for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append([i,j])

# bfs함수 
def bfs():
    while queue:
        x, y = queue.popleft() # 토마토 좌표
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomatoes[nx][ny] == 0:
                # 익히고 1을 더해준다.
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                queue.append([nx,ny])
            
bfs()
for i in tomatoes:
    for j in i:
        # 토마토 다 못익히면 -1
        if j == 0:
            print(-1)
            exit(0)
    # 다 익히면 최댓값
    res = max(res, max(i))

print(res-1) # 처음 시작한 부분 제외