#백준 - 피보나치 수 2
'''
입력 n
n번째 피보나치 수를 출력
'''
dp = [0]*91
dp[1] = 1
dp[2] = 1

n = int(input())
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2] # 점화식

print(dp[n])