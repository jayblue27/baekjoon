# 백준 - 수열(2419번) - 실버 4

N = int(input())
arr = list(map(int, input().split()))
dp1, dp2 = [1]*N, [1]*N # 오름, 내림 순열 각각 하나씩
for i in range(1, N):
    if arr[i] <= arr[i-1]:
        dp1[i] = max(dp1[i], dp1[i-1]+1)
    if arr[i] >= arr[i-1]:
        dp2[i] = max(dp2[i], dp2[i-1]+1)
print(max(max(dp1), max(dp2)))