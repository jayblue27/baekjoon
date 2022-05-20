# 백준 - 이친수 
'''
이친수(pinary number)
1.0으로 시작하지 않는다.
2.1이 두번연속 나타나지 않는다.

N이 주어졌을 때 N자리 이친수의 개수를 구하는 프로그램
-> 피보나치랑 같다
'''
import sys
input = sys.stdin.readline
N = int(input())

dp = [0] * 91
dp[1] = 1
dp[2] = 1

for i in range(3,N+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])