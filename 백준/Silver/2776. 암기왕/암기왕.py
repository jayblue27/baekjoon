# 암기왕 - 실버4
'''
하루동안 본 정수 기억 가능 

N개의 숫자 (1,000,000)
M개의 질문 (1,000,000)
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = set(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    for num in nums2:
        if num in nums1:
            print(1)
        else:
            print(0)

