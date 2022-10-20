def solution(triangle):
    triangle.reverse()
    dp = triangle[0]
    for i in range(len(triangle)):
        for j in range(len(triangle[i])-1):
            dp[j] = max(dp[j]+triangle[i+1][j],dp[j+1]+triangle[i+1][j])
    
    return dp[0]