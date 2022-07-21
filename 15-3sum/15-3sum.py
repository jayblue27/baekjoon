class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        ㅇ 문제
          1) 인덱스 중복x (한 세트 안에서)
          2) 세 수의 합은 0
          3) 숫자 list 형태로 return
          4) 해당하는 경우 없으면 0 return
          
        * 빗물보다 이게 더 어렵다;
        '''
        # #1) 부르트포스(내 풀이) -> 시간초과
        # ans = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 tmp = [nums[i],nums[j],nums[k]]
        #                 tmp.sort()
        #                 if tmp not in ans:
        #                     ans.append(tmp)
        # return ans
    
#         #2) 부르트포스(책 풀이) -> 시간초과
#         results = []
#         nums.sort()
        
#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             for j in range(i+1, len(nums)-1):
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
#                 for k in range(j+1, len(nums)):
#                     if k > j +1 and nums[k] == nums[k-1]:
#                         continue
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         results.append([nums[i], nums[j], nums[k]])
#         return results
        
        #3) 투 포인터 합계산
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):  
            # 중복값 생략
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 포인터 지정
            l, r = i+1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    results.append([nums[i],nums[l],nums[r]])
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        
        return results