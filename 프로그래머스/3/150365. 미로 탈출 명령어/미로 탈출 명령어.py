'''
1. 문제이해
- n(가로) x m(세로) 격자 미로
- x,y에서 출발 -> r,c로 탈출 

- 조건
    - 격자밖으로 탈출 불가
    - 총 이동거리가 k여야 한다. 
    - 탈출경로는 문자열로 나타냈을때 사전순으로 가장 빠른경로

2. 접근방법 
- 격자밖으로 탈출하지 않는, 이동거리가 k인 탈출경로 모두 추출
- 사전순으로 정렬하여 가장 빠른경로 추출
- 탈출경로 없는 경우 impossible
'''


from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    # 주어진 좌표에서 종료지점까지 남은거리 계산하는 함수 
    def manhattan(x1, y1):
        return abs(x1 - (r-1)) + abs(y1-(c-1))

    # k가 최단 거리보다 작거나, 최단 거리-k가 홀수라면 도착지에 k번만에 도착 불가
    if manhattan(x-1, y-1) > k or (manhattan(x-1, y-1) - k) % 2:
        return 'impossible'
    # 탐색 방향 사전순으로 - d l r u
    # 방향 자체를 사전순으로 정렬
    direct = {(1,0):'d', (0,-1):'l', (0,1):'r', (-1,0):'u'}
    q = deque()
    q.append((x-1, y-1, 0, ''))
    
    while q:
        si, sj, cnt, route = q.popleft()
        # 도착했는데 남은 거리가 홀수라면 도착지에 k만큼 오지 못한다! -> 왔다갔다 못하니까 2번 움직여야 하는데 1번만 남으니까
        if (si, sj) == (r-1, c-1) and (k-cnt) % 2:
            return 'impossible'
        
        # 도착하고 이동 거리가 k라면 현재까지의 경로 return
        elif (si, sj) == (r-1, c-1) and cnt == k:
            return route

        # 그 외에는 딕셔너리 순서대로 움직이면서
        for di, dj in direct:
                ni, nj = si+di, sj+dj
                # 지도 범위내에 있고
                if 0<=ni<n and 0<=nj<m:
                    # 새로 이동한 위치에서 도착위치 까지의 남은 이동 횟수가 k이상이라면 생략(k에 딱 맞춰서 움직여야 하니까)
                    # 다음 이동 자리를 보는 것이므로 +1 을 해주어야 함
                    if manhattan(ni, nj) + cnt + 1 > k:
                        continue
                    # 그외에는 q에 갱신값(새로운좌표, cnt갱신, 좌표갱신) append
                    q.append((ni, nj, cnt+1, route+direct[(di, dj)]))
                    break
    return answer
