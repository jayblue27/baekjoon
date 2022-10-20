import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

direction = [(1, 0), (0, 1)]    # 하 우
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == y == N-1:
            print(dp[x][y])
            exit(0)

        dist = graph[x][y]
        if x + dist < N:
            dp[x + dist][y] += dp[x][y]
        if y + dist < N:
            dp[x][y + dist] += dp[x][y]