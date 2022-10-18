#백준 - 이동하기
# n,m = 3, 4
# matrix = [[1,2,3,4],
#           [0,0,0,5],
#           [9,8,7,6]]

#입력
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))

#dp 초기화
dp = [[0]*m for _ in range(n)]
dp[0][0] = matrix[0][0]

#2중 반복문, 자기자신 전단계수를 더한값중 가장 큰값
for r in range(n):
    for c in range(m):
        if 0<= r <= n and 0 <= c-1 <= m:
            dp[r][c] = max(dp[r][c], dp[r][c-1] + matrix[r][c])
        
        if 0<= r-1 <= n and 0 <= c-1 <= m:
            dp[r][c] = max(dp[r][c], dp[r-1][c-1] + matrix[r][c])

        if 0<= r-1 <= n and 0 <= c <= m:
            dp[r][c] = max(dp[r][c], dp[r-1][c] + matrix[r][c])

#출력        
print(dp[-1][-1])       