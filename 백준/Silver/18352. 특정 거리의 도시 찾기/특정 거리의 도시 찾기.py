from collections import defaultdict, deque
import sys
input = sys.stdin.readline

#도시수(노드), 도로수(간선), target거리, 시작노드
n,m,k,x = map(int, input().split())
graph = defaultdict(list)

# 그래프 생성
for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2) 

visited = [False] * (n+1)
dist = [-1] * (n+1)

# 초기 설정
q = deque([(x,0)])
dist[x] = 0
visited[x] = True

# while 이용 bfs 진행 
while q:
    node, d = q.popleft()
    for v in graph[node]:
        if visited[v] == False:
            dist[v] = d+1
            visited[v] = True
            q.append((v, d+1))

if k not in dist:
    print(-1)
else:
    for i, n in enumerate(dist):
        if n == k:
            print(i)