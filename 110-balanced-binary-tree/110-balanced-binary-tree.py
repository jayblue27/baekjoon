# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        균형 이진트리 
        높이 균형(a height-balanced) : 모든 노드의 서브트리 간 높이 차이가 1이하인 것
        재귀구조로 푼다.
        '''
        # 책 풀이
        
        def check(root):
            if not root: 
                return 0 # false
            
            #왼쪽 오른쪽 check
            left = check(root.left)
            right = check(root.right)
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1증가
            if left == -1 or right  == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) +1
        
        return check(root) != -1
            
            
        
        