# 배열 합치기
'''
정렬된 두배열 A,B
합친 다음 출력
'''
from collections import deque

# 두 배열 A,B의 크기 N,M
N,M = map(int,input().split())
# A의 내용
A = list(map(int, input().split()))
# B의 내용
B = list(map(int, input().split()))

A.extend(B)
A.sort()
print(*A)