#백준 - 2*n 타일링
'''
1x2, 2x1로 채울수 있는 경우의 수 구하기
순서 0 1 2 3 4 5  6  7  8  9 
값   0 1 2 3 5 8 13 21 34 55

점화식 tile1=1, tile2=2, tile(n) = tile(n-1)+tile(n-2)
'''

import sys
input = sys.stdin.readline

dp = [0]*(1001)

dp[1] = 1
dp[2] = 2

n = int(input())
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] #점화식

print(dp[n]%10007) #출력조건