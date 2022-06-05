#백준 - 포도주 시식
'''
2579 계단오르기와 유사한 문제
d[i]는 i번째 포도주까지 최대로 마신 포도주의 양

특징
- 연속으로 놓여있는 3잔을 모두 마실 수 없다. 

경우의 수로 점화식 만들기
'''
import sys
input = sys.stdin.readline

N = int(input().rstrip())
wine = [0] * 10000

for i in range(N):
    wine[i] = int(input().rstrip())

dp = [0] * 10000
dp[0] = wine[0]
dp[1] = wine[0]+wine[1]
dp[2] = max(wine[2]+wine[0], wine[2]+wine[1], dp[1])

for i in range(3, N):
    dp[i] = max(wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3], dp[i-1])

print(max(dp))
    