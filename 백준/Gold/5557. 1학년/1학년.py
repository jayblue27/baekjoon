N = int(input())
NUM = list(map(int, input().split()))

dp = [[0]*(21) for _ in range(N)]
dp[0][NUM[0]]+=1

for idx in range(1, N-1):
    for result, count in enumerate(dp[idx-1]):
        if count:
            for new_result in (result+NUM[idx], result-NUM[idx]):
                if 0<=new_result<=20:
                    dp[idx][new_result] += count

print(dp[N-2][NUM[-1]])