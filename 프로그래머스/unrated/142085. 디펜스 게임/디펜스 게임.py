'''
1. n명 보유
2. 라운드 enemy[i] 마리의 적 등장
3. n중 enemy[i]만큼 소모하여 방어

dp로 풀어야할 것 같은 느낌 -> X
heap으로 풀이 ;;

'''
from heapq import heappushpop, heappush
def solution(n, k, enemy):
    # 무적권이 라운드수만큼 있으면 n의 개수와 무관하게 모든 라운드 통과가능
    if k == len(enemy):
        return k
    
    # 그 외
    heap = []
    total = round_ = 0
    for each in enemy:
        total += each
        if total <= n:
            heappush(heap, -each)
            round_ += 1
        elif k > 0:
            k -= 1
            total += heappushpop(heap, -each)
            round_ += 1
        else:
            break
    return round_ 
    
    
    
    