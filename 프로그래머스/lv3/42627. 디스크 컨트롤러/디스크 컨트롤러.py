# 정렬 , key 1, key 0
# 종료시간기준으로 단계 생성
# 시작시점에서 직전의 종료시점까지의 차를 더함


# 실패
# def solution(jobs):
#     answer = 0
#     end_point = 0

#     # 정렬
#     jobs.sort(key=lambda x:(x[1],x[0]))
    
#     for i, job in enumerate(jobs):
#         req_point = job[0]
#         duration = job[1]
        
#         if i == 0:
#             answer += duration
#             end_point += duration
#         else:
#             answer += duration + (end_point - req_point)
#             end_point += duration
    
#     return answer // len(jobs)

# 힙
# 우선순위의 기준은 무엇인가? 

import heapq
def solution(jobs): 
    answer, time, cnt = 0, 0, 0
    start = -1 
    heap = []
    jobs.sort()
    
    while cnt < len(jobs):
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(heap, [j[1], j[0]]) 
        
        if len(heap) > 0: 
            cur = heapq.heappop(heap)
            start = time
            time += cur[0]
            answer += time - cur[1] 
            cnt += 1
        else: 
            time += 1 
                
    return answer // len(jobs)
