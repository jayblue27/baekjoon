'''
유튜브 '송민기'님 풀이 참고
다익스트라 알고리즘으로 풀이

1. 최단경로 알고리즘
원래 다익스트라 알고리즘 -> 가중치의 합이 최소가 되는 경우
이 문제 
-> 가중치의 최댓값을 최소로 만들어라
-> 같은 intensity를 산봉우리가 여러개면, 번호가 작은 값을 반환

2. 모든 경로를 탐색하면 시간 복잡도 에러 발생 
node의 개수가 50000개 까지 있음 
다익스트라는 O(v^2)   (v:노드 수)
-> 우선순위 큐를 통해 최단거리 노드 찾는 부분 시간을 개선
-> 출입구를 출발지점, 산봉우리를 도착지점으로 하는 단방향 경로로 가정
'''
import heapq
import sys

def solution(n, paths, gates, summits):
    summits = set(summits)  # set 하고 안하고 왜이렇게 시간 차이 나지?
    # 등산경로 초기화
    graph = [[] for _ in range(n+1)]
    for i,j,w in paths: # i,j -> 노드숫자  / w -> 가중치
        # 등산경로 정보입력(양방향)
        graph[i].append((j,w))
        graph[j].append((i,w))
    
    # 다익스트라
    # gate 번호 앞에 0은 왜 넣는가? -> 우선순위 큐에서 가장 먼저 시작하기 위해
    pq = [(0, gate) for gate in gates]  # 우선순위 큐(pq), (현재까지의 intnesity, 현재 노드)
    
    INF = sys.maxsize # 혹은 10000001 -> 문제 조건에서 주어진 w 최대값(10,000,000) +1
    min_dis = [INF for _ in range(n+1)] # 최단 거리 테이블 초기화
    
    # 방문 처리 및 intensity 갱신
    while pq:
        intensity, node = heapq.heappop(pq) # 우선순위 큐에서, intensity가 낮은 순으로 하나씩 빼면서
        
        # 최단 거리 테이블에 주어진 값보다 intensity가 클경우 생략 (시간 효율 측면, min 연산 대신 continue로 생략)
        # in_dis[node] = min(min_dis[node], intensity) -> 시간초과 6개 발생
        if min_dis[node] <= intensity:  
            continue
        # 그외 경우 현재 intensity 값 갱신
        else: 
            min_dis[node] = intensity
            
        # 현재노드가 산봉우리면 진행하면 안됨
        if node in summits:
            continue
        
        # 다음 노드 정보 갱신
        for nxt, nxt_w in graph[node]:
            nxt_w = max(intensity, nxt_w)
            
            if min_dis[nxt] <= nxt_w:
                continue
            heapq.heappush(pq, (nxt_w, nxt))
    
    answer = [0, INF]
    
    
    # 정상들 순회하면서
    for summit in summits:
        # intensity 낮은 값으로 갱신
        if min_dis[summit] < answer[1]:
            answer[0], answer[1] = summit, min_dis[summit]
        # intensity가 같을 경우 낮은 번호 갱신
        elif min_dis[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit
            
    return answer
    