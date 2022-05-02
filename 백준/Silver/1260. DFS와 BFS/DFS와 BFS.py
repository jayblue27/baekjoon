# DFS와 BFS

# 다른 분의 풀이 보고 그대로 필사함
#https://junsik-hwang.tistory.com/75
# 그래프 자체에 대해서 공부하고 탐색 알고리즘 다시 공부

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램
# 정점이 여러개인 경우 정점 번호가 작은 것을 먼저 
# 더 이상 방문할 수 있는 점이 없을 경우 종료

# N : 정점의 개수, M: 간선의 개수, V : 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())

# 인접 영행렬
matrix = [[0] * (N+1) for i in range(N+1)]

# 방문한 곳 체크를 위한 배열 선언
visited = [0] * (N+1)

# 입력 받는 두 값에 대해 영행렬 1 삽입
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):
    # 방문한 곳에 1넣기
    visited[V] = 1
    print(V, end=' ')

    # 재귀 함수 선언(V와 인전한 곳을 찾고 방문하지 않았다면 함수 실행)
    for i in range(1, N+1):
        if(visited[i]==0 and matrix[V][i]==1):
            dfs(i)

def bfs(V):
    # 방문해야 할 곳을 순서대로 넣을 큐
    queue = [V]

    # dfs를 완료한 visited 배열(1로 되어있음)에서 0으로 방문체크
    visited[V] = 0

    # 큐 안에 데이터가 없을 때 까지 
    while queue:
        V = queue.pop(0)
        print(V, end = ' ')
        for i in range(1, N + 1):
            if(visited[i] == 1 and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0

dfs(V)
print()
bfs(V)