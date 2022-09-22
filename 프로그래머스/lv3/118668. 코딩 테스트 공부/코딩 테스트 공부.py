import sys
def solution(alp, cop, problems):
    # 목표값 : 모든 문제를 풀기위한 req 최대값
    alp_tgt = max([alp_req for alp_req , cop_req, alp_rwd, cop_rwd, cost in problems])
    cop_tgt = max([cop_req for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems])
    
    # (예외처리) 이미 모든 문제를 풀수 있으면 return 0
    if alp >= alp_tgt and cop >= cop_tgt:
        return 0 
    
    alp_tgt = max(alp_tgt, alp)
    cop_tgt = max(cop_tgt, cop)
    
    # 공부하는 것도 problems 형태로 변환 시켜준다
    problems.append([0,0,1,0,1]) # 알고력 1, cost 1
    problems.append([0,0,0,1,1]) # 코딩력 1, cost 1
    
    INF = sys.maxsize
    dp = [[INF for c in range(cop_tgt+1)] for r in range(alp_tgt + 1)]
    dp[alp][cop] = 0
    
    for r in range(alp, alp_tgt + 1):
        for c in range(cop, cop_tgt +1):
            # 문제를 못 푸는 조건
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if r < alp_req or c < cop_req:
                    continue
                nr, nc = min(r + alp_rwd, alp_tgt), min(c + cop_rwd, cop_tgt)
                dp[nr][nc] = min(dp[nr][nc], dp[r][c] + cost)
                
    return dp[-1][-1]