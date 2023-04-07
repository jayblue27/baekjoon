'''
1. board 크기와 동일한 방문처리 list 생성
2. 모든 좌표 순환하며 방문한적 없고, 울타리('#')아닌경우 bfs 실시
3. bfs 함수
    2번에 해당하는 좌표부터 방문 및 이동(이웃좌표)하며 방문처리 실시
    구역 내 양과, 늑대의 수를 세고 조건에 맞추어 전역변수에 해당하는 값을 더함
4. 최종 결과값 return 
'''

from collections import deque

# input data
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 방문처리 위한 리스트 생성 
visited = [[False] * C for _ in range(R)]

# 살아남은 양과, 늑대의 수를 세기위한 변수 선언
sheep_count = 0
wolf_count = 0

# 이동 좌표 생성
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs함수 정의
def bfs(r,c):
    # 함수 외부변수의 값을 변경해야하기 때문에 전역변수 설정
    global sheep_count, wolf_count 

    # 구역내 양과 늑대 수 카운팅을 위한 변수 초기화
    sheep = 0
    wolf = 0

    # 최초 좌표 q추가 및 방문처리
    queue = deque([(r, c)])
    visited[r][c] = True

    # 구역내 모든 좌표 순환
    while queue:
        r, c = queue.popleft()

        # 현재 좌표가 v면 늑대 추가
        if board[r][c] == 'v':
            wolf += 1
        # 현재 좌표가 k면 양 추가
        elif board[r][c] == 'k':
            sheep += 1

        # 이웃 방문처리
        for k in range(4):
            # 신규좌표에 대한
            nr, nc = r + dr[k], c + dc[k]
            # 범위 내 여부, 울타리 여부, 방문 여부 판단 후
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != '#' and not visited[nr][nc]:
                # q에 append 및 이웃(신규좌표) 방문처리
                queue.append((nr, nc))
                visited[nr][nc] = True

    # 구역 내 모든 방문 처리 실시 후
    # 양이 많은 경우 늑대가 잡아먹힘
    if sheep > wolf:
        sheep_count += sheep
    # 그 외에는 양이 잡아먹힘
    else:
        wolf_count += wolf

# 문제풀이
# 순환하면서 울타리(#)가 아니고, 방문한적이 없는 곳이면 방문시작
for r in range(R):
    for c in range(C):
        if board[r][c] != '#' and not visited[r][c]:
            bfs(r,c)

# 결과출력
print(sheep_count, wolf_count)