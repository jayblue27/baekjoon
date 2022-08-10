# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        이진 탐색 트리가 주어졌을때 L이상 R이하의 값을 지닌 노드의 합을 구하라
        '''
        #풀이 1 - 재귀 구조 DFS로 부르트포스 탐색
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)
        