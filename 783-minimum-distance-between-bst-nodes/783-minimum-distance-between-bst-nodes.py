# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        '''
        두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
        '''
        # 풀이 1 - 재귀 구조로 중위 순회
        prev = -sys.maxsize
        result = sys.maxsize
        
        # 재귀 구조 중위 순회 비교 결과
        def minDiffInBST(self, root: TreeNode) -> int:
            if root.left:
                self.minDiffInBST(root.left)
            
            self.result = min(self.result, root.val - self.prev)
            self.prev = root.val
            
            if root.right:
                self.minDiffInBST(root.right)
            
            return self.result
        
        # 풀이 2 - 반복 구조로 중위 순회
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        
        # 반복 구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
            
            node = node.right
        return result
        
        
        
        