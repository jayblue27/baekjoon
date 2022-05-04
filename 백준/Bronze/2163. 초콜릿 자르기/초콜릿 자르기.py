#초콜릿 자르기

# 1. 세로줄 자르기
# 3x3 -> 2번 / 3x4 -> 2번, N-1번

# 가로줄 자르기
# 3x3 -> 2번 / 3x4 -> 3번, M-1번  * N회

# 식
#(N-1) + ((M-1) * N)


def solution(N,M):
    ans = (N-1) + ((M-1) * N)
    return ans

import sys
input = sys.stdin.readline
N, M = map(int, input().split())

print(solution(N,M))
