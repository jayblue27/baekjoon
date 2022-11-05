from itertools import permutations
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()

for s in permutations(arr, m):
    print(*s)