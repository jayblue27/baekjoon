import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N): 
        u, a = input().split()
        arr.append([u,int(a)])
    arr.sort(key=lambda x:x[1], reverse=True)
    print(arr[0][0])
