import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

floating = [0] * 1000001

for height in arr:
    if floating[height] > 0:
        floating[height] -= 1
        floating[height - 1] += 1
    else:
        floating[height - 1] += 1

print(sum(floating))