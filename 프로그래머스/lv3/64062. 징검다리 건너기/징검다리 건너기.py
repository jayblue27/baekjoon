'''
기본적으로는 한칸씩
0이 생기면 최대 k칸 까지 건너뛸수 있음 
'''

def solution(stones, k):
    start = 1
    end = max(stones)
    mid = (start + end) // 2

    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
                if cnt >= k:
                    end = mid - 1
                    break
            else:
                cnt = 0
        else:
            start = mid + 1
    return start

# def solution(stones, k):
#     tmp = []
#     for i in range(len(stones)-k+1):
        
#         cnt = 0
#         for j in range(i, i+k):
#             if stones[i] >= stones[j]:
#                 cnt+=1
#         if cnt == k:
#             tmp.append(stones[i])
#     return min(tmp)

# # 연속되는 0의 개수를 세는 함수
# def continuous_num_count(arr, k):
#     cnt = 0     
    
#     tmp = 0
#     for num in arr:
#         if num <= k:
#             tmp += 1
#         else:
#             tmp = 0
        
#         cnt = max(cnt, tmp)
#     return cnt

# # 연속되는 0의 개수가 k개 일경우 더이상 건너뛸 수 없다 
# def solution(stones, k):
#     answer = 0
#     cnt = 0
    
#     max_num = max(stones)
#     for i in range(1, max_num+1):
#         if continuous_num_count(stones, i) == k:
#             return i
#     return i 
