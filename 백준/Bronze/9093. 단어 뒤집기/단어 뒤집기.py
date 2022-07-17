# 단어 뒤집기 - 브론즈 1

N = int(input())

for _ in range(N):
    T = input().split()
    for t in T:
        print(t[-1::-1], end=' ')