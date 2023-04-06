from collections import deque

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
sheep_count = 0
wolf_count = 0

for i in range(R):
    for j in range(C):
        if board[i][j] != '#' and not visited[i][j]:
            sheep = 0
            wolf = 0
            queue = deque([(i, j)])
            visited[i][j] = True

            while queue:
                r, c = queue.popleft()

                if board[r][c] == 'v':
                    wolf += 1
                elif board[r][c] == 'k':
                    sheep += 1

                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]

                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#' and not visited[nr][nc]:
                        queue.append((nr, nc))
                        visited[nr][nc] = True

            if sheep > wolf:
                sheep_count += sheep
            else:
                wolf_count += wolf

print(sheep_count, wolf_count)
