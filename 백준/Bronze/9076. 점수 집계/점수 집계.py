from collections import deque
T = int(input())

for _ in range(T):
    arr = list(map(int,input().split()))
    arr = deque(sorted(arr))
    arr.popleft()
    arr.pop()

    if (arr[-1] - arr[0]) >= 4:
        print('KIN')
    else:
        print(sum(arr))