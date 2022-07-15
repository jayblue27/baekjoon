class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        - target값을 만드는 두수 합의 위치 찾기
        - 똑같은 숫자 두번 쓸 수 없다. 
        
        ㅇ 접근법
          1) 부르트포스? 
          2) 
        '''
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                    