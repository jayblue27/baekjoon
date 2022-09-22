'''
유튜브 '송민기'님 풀이 참고
다익스트라 알고리즘으로 풀이

'''
import heapq

def solution(n, paths, gates, summits):
    # 등산경로 초기화
    summits = set(summits)
    conn = [[] for _ in range(n+1)]
    for i,j,w in paths:
        # 등산경로 정보입력
        conn[i].append((j,w))
        conn[j].append((i,w))
        
    # 다익스트라
    pq = [(0, gate) for gate in gates]
    w_MAX = 10000001
    min_dis = [w_MAX for _ in range(n+1)]
    
    while pq:
        intensity, node = heapq.heappop(pq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity
        if node in summits:
            continue
        for nxt, nxt_w in conn[node]:
            nxt_w = max(intensity, nxt_w)
            if min_dis[nxt] <= nxt_w:
                continue
            heapq.heappush(pq, (nxt_w, nxt))
    
    
    
    answer = [0, w_MAX]
    
    for summit in summits:
        
        if min_dis[summit] < answer[1]:
            answer[0], answer[1] = summit, min_dis[summit]
        elif min_dis[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit
            
    return answer
    