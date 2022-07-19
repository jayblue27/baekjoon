class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - target값을 만드는 두수 합의 위치 찾기
        - 똑같은 숫자 두번 쓸 수 없다. 
        
        ㅇ 접근법
          1) 부르트포스? 
          2) in을 이용한 탐색  
          3)
          4)
        '''
#         # 1) 부르트포스 - 7158ms
#         # 모든 조합 검색
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return i,j
        
        # 2) in을 이용한 탐색
        # (target - n) 값이 nums 안에 있는지 확인
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i+1:]:
                return [ nums.index(n), nums[i+1:].index(complement)+(i+1)]
        
#         # 3) 첫번째 수를 뺀 결과 키 조회
#         nums_map = {}
        
#         # 4) 
                    