'''
1. 문제이해
2. 접근방법
- 항상 종료지점까지 거리계산 (맨하탄 거리)
- 예외처리 2가지
    - 시작지점에서 종료지점까지의 거리가 k보다 큰 경우, k만에 종료지점에 도달하지 못하니까 'impossible' return 
    - (k - 최초 거리 계산값)의 결과가 홀수이면 'impossible' return (남은거리가 홀수면 종료지점에 도달 못함)
- 그 외
    - 알파벳 빠른순서대로 좌표 움직이면서
    - 다음좌표가 이동불가능(맵밖) 하거나, 다음좌표로 부터 종료지점까지의거리가 멀어지는게 아니라면
    - 
- 종료조건
    - 다음이동좌표가 end지점이고, 남은 k값이 0일때 
    
'''

from collections import deque
def solution(n, m, x, y, r, c, k):
    def cal_dist(r_now, c_now):
        return abs(r_now-r) + abs(c_now-c)
    
    if cal_dist(x,y) > k:
        return 'impossible'
    
    if (k - cal_dist(x,y)) % 2 == 1:
        return 'impossible'
    
    # 그 외의 경우  d l r u  -> 알파벳 순서대로 좌표 이동
    dic = {'d':(1,0), 'l':(0,-1), 'r':(0,1), 'u':(-1,0)}    
    path = ''
    q = deque([[x, y, k, path]]) 
    while q:
        x_now, y_now, k_now, path = q.popleft()
        # 현재 좌표가 도착지점에 도달하고 k가 0이면 현재까지의 경로 return
        if (x_now == r and y_now == c) and k_now == 0:
            return path
        
        # 그외 좌표이동
        for dirc, coor in dic.items():
            x_nxt = x_now + coor[0]
            y_nxt = y_now + coor[1]
            
            # 범위 내
            if 0 < x_nxt <= n and 0 < y_nxt <= m:
                if cal_dist(x_nxt, y_nxt) > k_now-1:
                    continue
                q.append([x_nxt, y_nxt, k_now-1, path+dirc])
                break
    
    return path