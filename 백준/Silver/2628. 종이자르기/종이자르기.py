# 종이자르기 - 실버5

import sys
input = sys.stdin.readline

x, y = map(int, input().split())
n = int(input())

x_arr = [0,x]
y_arr = [0,y]

for _ in range(n):
    xy, idx = map(int,input().split())
    if xy == 0:
        y_arr.append(idx)
    else:
        x_arr.append(idx)

# 좌표 오름차순 정렬
x_arr.sort()
y_arr.sort()

#좌표간 거리 구하기
x_dist = []
y_dist = []
for i in range(1, len(x_arr)):
    x_dist.append(x_arr[i]-x_arr[i-1])
for i in range(1, len(y_arr)):
    y_dist.append(y_arr[i]-y_arr[i-1])

#거리 내림차순 정렬
x_dist.sort(reverse=True)
y_dist.sort(reverse=True)

# 가장 큰 원소 곱하기
print(x_dist[0] * y_dist[0])