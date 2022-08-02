class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter + max heap
        freqs = collections.Counter(nums)
        freqs_heap = []
        
        # max heap(음수)로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))
        
        topk = list()
        
        # k번만큼 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk
        
        
        