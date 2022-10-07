#존수 계산 - 실버 2
'''
- 입력
전체 사람의 수(n) -> 노드 수 
촌수 계산 두사람의 번호 -> 시작점, 종료점

부모 자식들간 관계 개수(m) -> 그래프 정보
x,y -> 간선정보

'''
def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            dfs(i)

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 노드개수, 시작/종료노드 정보 확인
n = int(input())
start, end = map(int,input().split())

# 그래프 생성
m = int(input())
graph = [[] for _ in range(n+1)] # 초기화
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문처리 위한 리스트 생성 (1차원, 좌표는 2차원)
visited = [0] * (n+1)

dfs(start)

#출력
if visited[end]: print(visited[end])
else: print(-1)