# 백준 - 홀수
'''
7개 자연수
- 홀수의 합
- 최소 홀수
'''

import sys
input = sys.stdin.readline

lst = []
for _ in range(7):
    num = int(input())
    if num%2 != 0:
        lst.append(num)

if lst:
    print(sum(lst))
    print(min(lst))
else:
    print(-1)