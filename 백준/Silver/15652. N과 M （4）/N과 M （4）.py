def solution(N, M):
    res = []

    def backtracking(start):
        # breakpoint()
        
        if len(res) == M:
            print(' '.join(map(str, res)))
            return

        # N이 start 부터 시작 (1번과의 차이)
        for i in range(start, N + 1):
            res.append(i)
            backtracking(i)
            res.pop()

    backtracking(1)



if __name__ == "__main__":
    # N, M = 4, 2
    N, M = map(int, input().split())
    solution(N, M)
