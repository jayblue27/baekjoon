class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - nums[i] 빼고 나머지 요소 곱하기
        - 나눗셈 하지마라
        - O(n) 복잡도
        '''
#         import math 
#         # 1.  내 풀이 - 시간초과
#         # deque 써서 순환시키고 해당 숫자를 제외한 숫자끼리 곱한 값을 append
#         deq = deque(nums)
#         ans = []
#         for _ in range(len(nums)):
#             deq.append(deq.popleft())
#             ans.append(math.prod(list(deq)[:-1]))
            
#         return ans
        
        # 2. 책 풀이 
        out = []
        p =1
        
        for i in range(0, len(nums)):
            out.append(p)
            p = p *nums[i]
        p=1
        
        for i in range(len(nums)-1, 0-1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        
        return out
        
        
        
            
            
            
            
        
            
        
        
            
            
            
            