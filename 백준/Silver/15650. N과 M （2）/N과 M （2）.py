def DFS(start):
    if len(s) == M: 
        print(' '.join(map(str, s)))
        return

    for i in range(start, N + 1):
        if i not in s:
            s.append(i)
            DFS(i+1)
            s.pop()

N, M = map(int, input().split())
s = []
DFS(1)