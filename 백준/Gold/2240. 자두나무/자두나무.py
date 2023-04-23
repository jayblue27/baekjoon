T, W = map(int, input().split())

# dp[i][j]: i번째 초에 나무 j에서 j번 움직였을 때 최대 자두 개수
dp = [[0] * (W + 1) for _ in range(T + 1)]

# 1초부터 T초까지
for i in range(1, T + 1):
    # 현재 나무 번호
    tree = int(input())

    # 이전 초에서 움직인 횟수를 그대로 유지할 경우
    for j in range(W + 1):
        if tree == 1:
            # 이전 나무가 1번일 때, 현재 나무가 1번인 경우
            # dp[i][j]는 dp[i - 1][j]에서 자두 개수 + 1을 하거나 그대로인 경우 중 큰 값
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + (1 if j % 2 == 0 else 0))
        else:
            # 이전 나무가 2번일 때, 현재 나무가 2번인 경우
            # dp[i][j]는 dp[i - 1][j]에서 자두 개수 + 1을 하거나 그대로인 경우 중 큰 값
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + (1 if j % 2 == 1 else 0))

    # 이전 초에서 움직인 횟수를 하나 늘릴 경우
    for j in range(1, W + 1):
        if tree == 1:
            # 이전 나무가 1번일 때, 현재 나무가 2번인 경우
            # dp[i][j]는 dp[i - 1][j - 1]에서 자두 개수 + 1을 하거나 그대로인 경우 중 큰 값
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (1 if j % 2 == 1 else 0))
        else:
            # 이전 나무가 2번일 때, 현재 나무가 1번인 경우
            # dp[i][j]는 dp[i - 1][j - 1]에서 자두 개수 + 1을 하거나 그대로인 경우 중 큰 값
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (1 if j % 2 == 0 else 0))

# 최대 자두 개수
max_count = 0
for j in range(W + 1):
    max_count = max(max_count, dp[T][j])

print(max_count)
