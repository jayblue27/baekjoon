dp = [0] * int(10e6 +1)
def make_one(k):
    for i in range(2,k+1):
        # 3. 1을 뺀다. 
        dp[i] = dp[i-1] + 1
           
        if i%2 == 0:
            #    2         1         
            dp[i] = min(dp[i], dp[i//2]+1 )
        if i%3 == 0 :
            dp[i] = min(dp[i], dp[i//3]+1)
        
    return dp[k]

N = int(input())
print(make_one(N))