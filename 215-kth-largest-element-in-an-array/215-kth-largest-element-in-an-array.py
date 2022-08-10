class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        정렬되지 않은 배열에서 k번째 큰 요소를 추출하라. 
        '''
#         # 풀이 1 - heapq모듈 이용 - 882ms
#         heap = list()
#         for n in nums:
#             heapq.heappush(heap, -n)
        
#         for _ in range(1, k):
#             heapq.heappop(heap)
            
#         return -heapq.heappop(heap)
    
#         # 풀이 2 - heapq 모듈의 heapify 이용 - 991ms
#         heapq.heapify(nums)
        
#         for _ in range(len(nums) - k):
#             heapq.heappop(nums)
            
#         return heapq.heappop(nums)
    
#         # 풀이 3 - heapq 모듈의 nlargest 이용 - 1010ms
#         return heapq.nlargest(k, nums)[-1]
    
        # 풀이 4 - 정렬을 이용한 풀이
        return sorted(nums, reverse=True)[k-1]
    
    
        