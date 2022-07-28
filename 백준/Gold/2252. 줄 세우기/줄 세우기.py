# 백준 - 줄 세우기
from heapq import *
from collections import deque

# 위상정렬
v, e = map(int, input().split())

# 진입차수 초기화
indegree = [0] * (v+1)
# 그래프 초기화
graph = [[] for i in range(v+1)]

# 그래프의 간선 정보 입력 받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수 증가
    indegree[b] += 1

result = []
q = deque()

for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)
print(*result)
