import sys
import heapq

# # 다익스트라 알고리즘
# def dijkstra(s, e):
#     global graph, length
    
#     # 방문한 노드를 최대값으로 세팅
#     visit = [sys.maxsize]*(length+1)
    
#     # start node는 0으로 바꾸어주고
#     visit[s] = 0
    
#     # 우선순위힙큐에 [cost, node]로 넣어준다
#     pq = [[0, s]]
    
#     heapq.heapify(pq)
    
#     # bfs 진행
#     while pq:
#         cost, node = heapq.heappop(pq)
        
#         # 해당노드를 방문하는데 드는 비용이 기존 최소비용보다 큰 경우는 무시
#         if cost > visit[node]:
#             continue
        
#         # 그 다음 방문 가능한 노드 탐색
#         for i in graph[node]:
#             new_node, new_cost = i[0], i[1]
            
#             # 기존의 비용에 cost 추가해서 새로운 비용
#             new_cost += cost
            
#             # 만약 새로운 비용이 기존의 방문노드를 방문하는데 드는 비용보다 작을 경우만 진행
#             if new_cost < visit[new_node]:
#                 # 방문노드 값을 갱신
#                 visit[new_node] = new_cost
                
#                 # heapq에 넣어주고 계속 진행
#                 heapq.heappush(pq, [new_cost, new_node])
    
#     return visit[e]

# def solution(n, s, a, b, fares):
#     global graph, length
    
#     answer = sys.maxsize
#     graph = [[] for _ in range(n+1)]
#     length = n
    
#     for i, j, cost in fares:
#         graph[i].append([j, cost])
#         graph[j].append([i, cost])
            
#     for i in range(1, n+1):
#         answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
#     return answer

# 플로이드 워셜 전체탐색 
# 효율성 테스트 133.82ms ~ 1168.50ms 
'''
n : 노드의 개수
s : 출발지점
a : a 도착지점
b : b 도착지점
farees : [시작노드, 종료노드, 가격]
'''

import sys
INF = sys.maxsize 

# 플로이드 워셜 : 모든 노드 간 최단 경로 구성가능
def floyd(dist, n):
    # 3중 for문 O(n^3)
    for k in range(n): # 경유지 노드
        for i in range(n): # 출발지 노드
            for j in range(n): # 도착지 노드
                
                # dist[i][j] : i에서 j까지 가는 요금
                # dist[i][k] + dist[k][j]  : i에서 j까지 가는데 k를 경유해서 가는 경우 요금
                if dist[i][k] + dist[k][j] < dist[i][j]: # k를 경유해서 가는 요금이 싼 경우 
                    dist[i][j] = dist[i][k] + dist[k][j] # i->j 값을 업데이트 해준다. (최종적으로 최소 비용이 적용 됨)

def solution(n, s, a, b, fares):
    # 노드 및 노드간 요금 초기화
    dist = [[INF for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        dist[i][i] = 0 # 자기자신은 요금이 0
    
    for edge in fares: 
        # 노드의 방향정보가 없기 때문에 양방향으로 같은 요금을 지정해준다.
        dist[edge[0]-1][edge[1]-1] = edge[2] 
        dist[edge[1]-1][edge[0]-1] = edge[2]
        
    # 플로이드 워셜 알고리즘
    floyd(dist, n)
    # print(dist)
    
    # 문제에서는 노드번호가 1부터 시작하기 때문에 
    # 파이썬 인덱싱 번호에 맞춰 1씩 빼준다. 
    s -= 1
    a -= 1
    b -= 1
    
    answer = INF # 초기값
    
    for k in range(n):
        # dist[s][k] : s(시작노드)에서 k 까지(합승) 요금
        # dist[k][a] : 합습 종료지점에서 a지점 까지 요금
        # dist[k][b] : 합습 종료지점에서 b지점 까지 요금
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])  # 최소값 갱신
    
    return answer