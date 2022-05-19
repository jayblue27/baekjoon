import sys
read = sys.stdin.readline

N = int(read())
A = [0] + list(map(int, read().split()))
cache = [0] * (N+1)
cache[1] = 1

for i in range(2, N+1):
    temp = []
    for j in range(1, i):
        if A[j] < A[i]:
            temp.append(cache[j])
    cache[i] = max(temp) + 1 if temp else 1
print(max(cache))