from itertools import combinations
import math
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cmd = list(map(int, input().split()))
    n, arr = cmd[0], cmd[1:]

    ans = 0
    for x,y in list(combinations(arr,2)):
        ans += math.gcd(x,y)
    print(ans)