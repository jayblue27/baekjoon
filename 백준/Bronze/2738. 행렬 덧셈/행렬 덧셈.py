# 행렬 덧셈 - 백준 - 브론즈 5

# 입력
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

# 계산
for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for line in A:
    print(*line)