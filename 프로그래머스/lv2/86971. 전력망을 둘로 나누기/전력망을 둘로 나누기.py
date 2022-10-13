'''
wires는 n-1 길이고
전력망 네트워크가 하나의 트리 형태가 아닌 경우 입력으로 주어지지 않는다고 했으니
노드의 숫자는 1부터 연속된 숫자이다.

1. wires의 간선정보를 하나씩 건너 뛰며 그래프를 만든다. 
2. 1번에서 만든 그래프를 dfs를 통해 1번부터 시작하는 전력망의 노드개수를 구한다. 
3. 2번에서 구한값(A전력망의 수) n에서 A전력망의 수를 뺀 수(B전력망의 수)를 구하고
   A전력망수 - B전력망수 의 절대값을 계산하여 갱신한다.
4. 3번의 값을 return 한다. 
'''

def solution(n, wires):
    result = 100 # n이 100이하 자연수
    # 1. 간선정보 하나씩 건너뛰며 그래프 만들고
    for i in range(1,n):
        # global graph
        graph = [[] for _ in range(n+1)] # 1~n번 까지의 빈 그래프 생성
        for j in range(1, n):
            a,b = wires[j-1][0], wires[j-1][1]
            if i==j: continue  
            graph[a].append(b)
            graph[b].append(a)
        
        # 2. dfs통해서 1번부터 시작하는 전력망의 노드개수 구한다.
        cnt = dfs(1, graph)
        # 3. a,b 전력망 크기의 차이 최소값을 갱신한다.
        result = min(result, abs(cnt - (n-cnt)))
    
    return result


# dfs를 통해 graph에 연결된 node의 개수 카운트
def dfs(v,graph):
    visited = set()
    stack=[v]
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.add(now)
            
            # now에 연결된 노드들을 탐색
            for nv in graph[now]:
                stack.append(nv)
    
    return len(visited) # 첫번째 연결된 노드의 수 반환