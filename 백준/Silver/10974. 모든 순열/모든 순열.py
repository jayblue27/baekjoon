import itertools

N = int(input())
arr = list(itertools.permutations([x for x in range(1,N+1)], N))
for x in arr:
    print(*x)