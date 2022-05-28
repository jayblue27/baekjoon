#백준 - 일곱 난장이

import sys
input = sys.stdin.readline
from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

combination = combinations(arr, 7)
for k in combination:
    if sum(k) == 100:
        k_list = list(map(int, k))
        k_list.sort()
        for i in k_list:
            print(i)
        break