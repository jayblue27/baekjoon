#백준 - 2*n 타일링 2
'''
입력 n
2*n 타일 
1x2, 2x1, 2x2로 채울수 있는 경우의 수 구하기
순서 0 1 2 3     
값   0 1 3 5    

점화식 tile1=1, tile2=3, tile(n) = tile(n-1)+ 2* tile(n-2)
결과를 10007로 나눠준 값을 출력
'''

dp = [0]*1001

dp[1] = 1
dp[2] = 3
n = int(input())

for i in range(3,n+1):
    dp[i] = dp[i-1] + (2*dp[i-2]) #점화식

print(dp[n]%10007) #출력조건