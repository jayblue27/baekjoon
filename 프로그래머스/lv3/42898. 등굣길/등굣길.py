def solution(m, n, puddles):
    # 지도 초기화
    maps = [[0]*(m+1) for _ in range(n+1)]
    maps[1][1] = 1
    
    # 웅덩이 생성
    for r, c in puddles:
        maps[c][r] = -1
    
    # 순회
    for r in range(1,n+1):
        for c in range(1,m+1):
            if maps[r][c] == -1:
                continue
            maps[r][c] = max(maps[r][c], maps[r-1][c], maps[r][c-1], maps[r-1][c]+maps[r][c-1])
        
    return maps[-1][-1] % 1000000007

