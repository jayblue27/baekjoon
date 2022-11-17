# 풀이시도 - 완전탐색 (10,12,13 통과) 그외 전부 실패, 효율성 실패
# import sys
# from itertools import combinations_with_replacement
# def solution(n, works):
    
#     if sum(works) <= n:
#         return 0
#     tmp = sum(works) - n
#     max_works = max(works)
#     tmp_list = list(range(max_works+1))
    
#     tmp_val_list = set()
#     for tup in combinations_with_replacement(tmp_list, len(works)):
        
#         if sum(tup) == tmp:
#             tmp_val=0
#             for t in tup:
#                 tmp_val += t**2
#             tmp_val_list.add(tmp_val)
            
#     return min(tmp_val_list)
            

# for문 이용 큰수를 1씩 줄이기
# for문 만큼 정렬이 되어야 함 n * nlogn -> 효율성 실패
# def solution(n, works):
#     if sum(works)<=n:
#         return 0
            
#     works.sort()
#     for _ in range(n):
#         works[-1]-=1
#         works.sort()
#     return sum([i**2 for i in works])

# heap으로 정렬 자동화
import heapq

def solution(n, works):
    #예외 처리 - 케이스 3
    if sum(works)<=n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    
    return sum([i**2 for i in works])
    
    



    