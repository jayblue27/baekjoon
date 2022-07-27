N, M = map(int, input().split())

S = []
for _ in range(N):
    S.append(input())

M_str = []
cnt = 0
for _ in range(M):
    tmp = input()
    if tmp in S:
        cnt += 1

print(cnt)