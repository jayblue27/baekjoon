#백준 - 카드 구매하기
'''
비싼 카드가 높은 등급이 많이 들어있을거라고 믿는다.

점화식 : dp[i] = p[j] + dp[i - j]
'''

#입력
# N : 구매하려고 하는 카드의 개수
N = int(input())
# P : n장의 카드 구매 가격
P = [0] + list(map(int, input().split()) )
dp = [0] * (N+1)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + P[j])

print(dp[i])