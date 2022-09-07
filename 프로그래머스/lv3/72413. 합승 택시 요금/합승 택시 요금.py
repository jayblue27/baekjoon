import sys
import heapq

# 다익스트라 알고리즘
def dijkstra(s, e):
    global graph, length
    
    # 방문한 노드를 최대값으로 세팅
    visit = [sys.maxsize]*(length+1)
    
    # start node는 0으로 바꾸어주고
    visit[s] = 0
    
    # 우선순위힙큐에 [cost, node]로 넣어준다
    pq = [[0, s]]
    
    heapq.heapify(pq)
    
    # bfs 진행
    while pq:
        cost, node = heapq.heappop(pq)
        
        # 해당노드를 방문하는데 드는 비용이 기존 최소비용보다 큰 경우는 무시
        if cost > visit[node]:
            continue
        
        # 그 다음 방문 가능한 노드 탐색
        for i in graph[node]:
            new_node, new_cost = i[0], i[1]
            
            # 기존의 비용에 cost 추가해서 새로운 비용
            new_cost += cost
            
            # 만약 새로운 비용이 기존의 방문노드를 방문하는데 드는 비용보다 작을 경우만 진행
            if new_cost < visit[new_node]:
                # 방문노드 값을 갱신
                visit[new_node] = new_cost
                
                # heapq에 넣어주고 계속 진행
                heapq.heappush(pq, [new_cost, new_node])
    
    return visit[e]

def solution(n, s, a, b, fares):
    global graph, length
    
    answer = sys.maxsize
    graph = [[] for _ in range(n+1)]
    length = n
    
    for i, j, cost in fares:
        graph[i].append([j, cost])
        graph[j].append([i, cost])
            
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))
        
    return answer