# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        '''
        오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라
        높이 균형 : 두 서브 트리 간 깊이 차이가 1이하 
        BST 정렬되어 있어야 한다. 
        '''
        if not nums:
            return None
        
        mid = len(nums) // 2 # 내림값 
        
        # 분할 정복으로 이진 검색 결과 트리 구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node
        