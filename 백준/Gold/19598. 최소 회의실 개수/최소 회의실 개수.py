from sys import stdin
import heapq

N = int(stdin.readline())
confs = []
for _ in range(N):
    s, e = map(int, stdin.readline().split())
    confs.append((s, e))
confs.sort(key=lambda x : (x[0],x[1]))

rooms_end = [0]
for start, end in confs:
    if start>=rooms_end[0] : heapq.heappushpop(rooms_end, end)
    else : heapq.heappush(rooms_end, end)
print(len(rooms_end))