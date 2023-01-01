# 동전 - 골드5
T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [1] + [0] * M

    for coin in coins:
        for i in range(coin, M+1):
            dp[i] = dp[i-coin] + dp[i]
    
    print(dp[-1])