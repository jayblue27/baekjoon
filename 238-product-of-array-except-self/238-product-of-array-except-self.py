class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        - nums[i] 빼고 나머지 요소 곱하기
        - 나눗셈 하지마라
        - O(n) 복잡도
        '''
        # 1.  내 풀이 - 나눗셈 
        
        
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
        
        
        
            
            
            
            
        
            
        
        
            
            
            
            