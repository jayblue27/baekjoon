import sys
import math

# 입력
input = sys.stdin.readline
N, K = map(int, input().split())

ans = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))
print(ans)