# 가장 긴 감소하는 부분 수열
'''
수열 A 가장 긴 감소하는 부분 수열을 구하는 
감소
'''
n=int(input())
A=list(map(int, input().split()))
dp=[1]*n
for i in range(n):
    for j in range(i):
        if A[j]>A[i]:
            dp[i]=max(dp[i], dp[j]+1)
print(max(dp))