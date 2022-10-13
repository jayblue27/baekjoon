# 연구소 - 골드 4
'''
N*M 크기의 연구소

1. 연구소내 0인 좌표 담기 -> 잠재적으로 벽 세울 공간 
2. combinations로 3개의 좌표를 선정해서 벽을 세운다(해당 좌표에 1을 넣는다.)
3. 2중 for문으로 연구소 전체 순환하며 바이러스를 퍼트린다.
4. 영역별 가장 큰 안전 영역의 개수 갱신
'''
from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

# n,m = 7, 7
# lab = [[2,0,0,0,1,1,0],
#         [0,0,1,0,1,2,0],
#         [0,1,1,0,1,0,0],
#         [0,1,0,0,0,0,0],
#         [0,0,0,0,0,1,1],
#         [0,1,0,0,0,0,0],
#         [0,1,0,0,0,0,0]]

#0. 입력받기
n,m = map(int, input().split())
lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))



#1. 값이 0, 2인 좌표 담기
crd_0 = []
crd_2 = []
for r in range(n):
    for c in range(m):
        if lab[r][c] == 0: crd_0.append((r,c))
        if lab[r][c] == 2: crd_2.append((r,c))

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def virus(r, c):
    '''바이러스 퍼트리기'''
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if (0 <= nr < n) and (0 <= nc < m):
            if new_lab[nr][nc] == 0:
                new_lab[nr][nc] = 2
                virus(nr,nc)

def safe_zone(arr):
    '''안전영역 개수 구하고 반환'''
    cnt = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 0: 
                cnt+=1
    return cnt

#2. combinations 3개 좌표 선정해서 1 넣기
combi_crd_0 = list(combinations(crd_0, 3)) # 6545가지
result = 0

for cases in combi_crd_0:
    new_lab = deepcopy(lab) 

    # 3개의 벽 세우기
    for r, c in cases:
        new_lab[r][c] = 1
    
    # 3. 바이러스 퍼트리기
    for r, c in crd_2:
        virus(r,c)

    # 4. 0개수 세고 최대값 갱신하기
    result = max(result, safe_zone(new_lab))

print(result)  