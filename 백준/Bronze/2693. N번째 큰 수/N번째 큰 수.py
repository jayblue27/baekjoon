n = int(input())

for _ in range(n):
    A = list(map(int,input().split()))
    print(sorted(A)[-3])
    