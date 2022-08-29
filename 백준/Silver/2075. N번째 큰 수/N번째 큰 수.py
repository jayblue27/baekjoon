#백준 - N번째 큰 수

import heapq

n = int(input())
total_list = []
for i in map(int, input().split()):
    heapq.heappush(total_list, i)

for i in range(1, n):
    a = list(map(int, input().split()))
    for j in range(n):
        if a[j] > total_list[0]:
            heapq.heappush(total_list, a[j])
            heapq.heappop(total_list)
print(total_list[0])