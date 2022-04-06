# pypy3 아니고 python3 선택시 시간초과
lst = []
N = int(input())

for _ in range(N):
    lst.append(int(input()))

lst = sorted(lst)

for i in range(N):
    print(lst[i])