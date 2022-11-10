'''
dp?
아이디어라도 떠올려 ㅂ자 

무조건 짧은 길이 정답이 아니다

1. 출발지에서 목적지까지 가는 모든 경로를 구한다. (가능하면 직선, 코너 수를 카운팅)
2. 모든 경로의 건설비용을 계산한다.
3. 건설비용이 가장 적은 경로를 return한다.
'''
def solution(board):
    answer = 0
    return answer

from collections import deque


def solution(board):
    n = len(board)
    answer = int(1e9)
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]
    # 현재 지나간 길을 확인하기 위한 idx 추가
    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
    # i, j, cost, direction
    q = deque([(0, 0, 0, -1)])
    while q:
        i, j, cost, dir_idx = q.popleft()
        # 정답 범위이고, 현재 cost가 더 적을 때 값 할당
        if (i, j) == (n - 1, n - 1) and answer > cost:
            answer = cost
        for direction in directions:
            # 다음 값 셋팅
            next_i = i + direction[0]
            next_j = j + direction[1]
            add_cost = 1 if dir_idx == direction[2] or dir_idx == -1 else 6
            # 현재 값 판단할 지 여부
            if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
                continue
            if dp[next_i][next_j] < cost + add_cost - 4:
                continue
            # dp에 값 설정 및 큐에 추가
            dp[next_i][next_j] = cost + add_cost
            q.append((next_i, next_j, cost + add_cost, direction[2]))
    return answer * 100