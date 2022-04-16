#점화식 n = n-2 + n-3
dp = [0] * 101
def padoban(n):
    if n == 1 or n == 2 or n==3:
        return 1
    
    
    dp[1] = dp[2] = dp[3] = 1    
    
    if dp[n] != 0:        
        return dp[n]
    
    for i in range(4,n+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(input())
for _ in range(T):
    N = int(input())
    print(padoban(N))