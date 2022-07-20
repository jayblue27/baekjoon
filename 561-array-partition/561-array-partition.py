class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''        
        2n 길이
        nums 숫자 오름차순 정렬하고 
        홀수번째 숫자의 합 더한다.        
        
        '''
#         # 1) 내 풀이 - 480ms 
#         # nums 오름차순 정렬
#         nums.sort()
        
#         # 0번부터 2칸씩 증가하며 덧셈 실시
#         # 
#         ans = 0 
#         for i in range(0,len(nums),2):
#             ans += nums[i]
        
#         return ans
    
        # 2) 파이써닉한 풀이(책3번) - 오.. 
        return sum(sorted(nums)[::2])
        
        
        