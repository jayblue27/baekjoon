import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = input()
    n_list = [*map(int, input().split())]
    m = input()
    m_list = [*map(int, input().split())]

    # n_list 정렬
    n_list.sort()

    for i in m_list:        
        # left와 right가 같은 경우 0, 그 외 1
        if bisect_left(n_list, i) == bisect_right(n_list, i):
            print(0)
        else:
            print(1)