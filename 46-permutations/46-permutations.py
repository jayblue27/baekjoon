class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #풀이 1 : DFS - 48ms
        results = []
        prev_elements = []
        
        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0: # elements 길이가 0인게 왜 리프노드인가 나중에 확인
                results.append(prev_elements[:])
            
            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]  # [1,2,3] / 
                next_elements.remove(e) # [2,3]
                
                prev_elements.append(e) # [1]
                dfs(next_elements) # dfs([2,3])
                prev_elements.pop() # 
        
        dfs(nums)
        return results
    
        #풀이 2 : itertools - 45ms
        return list(itertools.permutations(nums))
        