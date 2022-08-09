# 백준 - 여행 가자 - 골드 4
'''
도시가 N개
두 도시 사이에 길이 있을 수도, 없을 수도 있다. 
여행 일정이 주어졌을때, 이경로가 가능한 것인지 
같은 도시 여러번 방문 가능

ㅇ 입력
도시의 수 N   200이하
여행에 속한 도시들의 수 M   1000이하
N개의 - i번째 줄의 j번째 수, 
마지막 여행 계획

ㅇ 출력
가능하면 YES
아니면 NO

ㅇ 접근법
서로소 집합(교집합이 없는 두 집합) - 서로 관계 없음
- 그래프 간선정보 생성
- 유니온 파인드 이용 특정 노드부터 특정 노드까지 이어져있는지 확인 가능
'''

import sys
input = sys.stdin.readline
del input

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
    
def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

# 유니온 파인드
n,m = int(input()),int(input())
parents = [i for i in range(n)]
for i in range(n):
    link = list(map(int,input().split()))
    for j in range(n):
        if link[j] == 1:
            union(i,j)

# 특정 원소가 속한 집합을 찾기
def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 경로 체크
parents = [-1] + parents
path = list(map(int,input().split()))
start = parents[path[0]]
for i in range(1,m):
    if parents[path[i]] != start:
        print("NO")
        break
else:
    print("YES")