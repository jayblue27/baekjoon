#백준 - 정수 삼각형 

import sys 
input = sys.stdin.readline

#입력
n = int(input())
triangle = []
for i in range(n):
    triangle.append(list(map(int,input().split())))

#탐색하며 값을 변경해간다
triangle[0][0]
for i in range(1, len(triangle)):
    for j in range(i+1):
        if j == 0:
            triangle[i][j]+=triangle[i-1][j]
        elif j == i:
            triangle[i][j]+=triangle[i-1][j-1]
        else:
            triangle[i][j]+=max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[-1]))