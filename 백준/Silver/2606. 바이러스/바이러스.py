# 백준 - 바이러스 - DFS

#입력
# 컴퓨터의수, 직접 연결되어있는 컴퓨터쌍의 수 
N = int(input())
graph = [[]*N for _ in range(N+1)]
# 직접 연결되어 있는 컴퓨터 번호쌍
M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(N+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1

# 1번 컴퓨터  
dfs(1)
print(cnt)