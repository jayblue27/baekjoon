N = int(input())
# 문제접근
# 1. 규칙찾아 dp 생성하기
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 1

for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]
# 2. 둘레 구하기 : 현재의 한변길이 * 2 + (현재+직전) *2 
ans = (dp[N] * 2) + ((dp[N] + dp[N-1])*2)
print(ans)