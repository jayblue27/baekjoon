# 백준 - 최대 힙
'''
heapq 모듈에서는 최소힙만 구현
자연수 앞에 -를 넣어서 최대힙으로 구현한다. 
'''
import sys
import heapq
input = sys.stdin.readline

#입력
N = int(input())
heap = []

#최대힙
for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)