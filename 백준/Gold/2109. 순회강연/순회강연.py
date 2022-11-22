import sys
import heapq
n = int(input())
money = 0
arr = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    arr.append([tmp[0],tmp[1]])

arr = sorted(arr,key=lambda x: (x[1])) 

queue = []

for pay,day in arr:
    heapq.heappush(queue,pay)

    if day < len(queue): 
        heapq.heappop(queue) 

print(sum(queue))