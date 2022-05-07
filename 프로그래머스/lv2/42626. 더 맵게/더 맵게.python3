# 프로그래머스 - 더 맵게
import heapq
def solution(scoville, K):
    '''
    섞은 음식의 스코빌 지수 
    = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
    
    모든 스코빌지수가 K이상 되려면 몇번 섞어야 하나
    '''
    answer = 0
    heapq.heapify(scoville)    

    # 첫번째 요소가 K 미만일 때
    while scoville[0] < K:
        # 주어진 계산식대로 혼합
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2) # pop해서
        # print(mix)
        heapq.heappush(scoville, mix)  # push
        # print(scoville)
        answer += 1 # 횟수증가
        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7

solution(scoville, K)