import sys; input = sys.stdin.readline

N = int(input())
a = sorted(map(int, input().split()))

# 홀수 + 홀수 = 짝수
result = odd = 0
for i in range(N - 1, -1, -1): # 사탕 묶음의 개수가 큰 것부터 시작
    if a[i] & 1: # 홀수면 따로 빼두자.
        if odd: # 만약 따로 빼둔 홀수가 이미 있으면 홀수끼리 더해서 결과에 더하자.
            result += odd + a[i]
            odd = 0
        else:
            odd = a[i]
    else: # 짝수면 바로 결과에 더하자.
        result += a[i]

print(result)