#백준 - 연속합 
'''
n개의 정수 임의 수열
연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구한다.
'''
#입력
n = int(input())
arr = list(map(int, input().split()))

#출력
dp = [0] * len(arr) 
dp[0] = arr[0] 

# 해당 자리의 숫자중 가장 큰 값으로 대체
for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

# 가장 큰 경우 출력
print(max(dp))