import sys
from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    C = list(sys.stdin.readline().split())
    if len(C) == 2:
        queue.append(int(C[1]))
    
    elif C[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif C[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    elif C[0] == 'size':
        print(len(queue))

    elif C[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif C[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())