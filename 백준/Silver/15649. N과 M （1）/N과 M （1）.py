from itertools import permutations
N, M = map(int, input().split())
arr = list(permutations(list(range(1,N+1)),M))
for i in arr:
    print(*i)