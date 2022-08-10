class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        정렬되지 않은 배열에서 k번째 큰 요소를 추출하라. 
        '''
        # 풀이 1 - heapq모듈 이용
        heap = list()
        for n in nums:
            heapq.heappush(heap, -n)
        
        for _ in range(1, k):
            heapq.heappop(heap)
            
        return -heapq.heappop(heap)
        