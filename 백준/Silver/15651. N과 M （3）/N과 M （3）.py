def solution(N,M):
    res = []
    v = [False] * (N+1)

    def backtracking(num):
        # breakpoint()
        # 종료 조건
        if num == M:
            print(' '.join(map(str, res)))
            return
        for i in range(1, N+1):
            if not v[i]:
                # v[i] = True
                res.append(i)
                backtracking(num+1) #하나씩 늘려감 
                # v[i] = False
                res.pop()
    backtracking(0)
N,M = map(int,input().split())
# N, M = 4, 2
solution(N,M)