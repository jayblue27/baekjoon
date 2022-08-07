# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 풀이 1 - pythonic code
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None
    
        # 풀이 2 - 반복 구조로 BFS
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            #부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                quene.append(node.right)
        
        return root
    
#         # 풀이 3 - 반복 구조로 DFS - 31ms
#         stack = collections.deque([root])
        
#         while stack:
#             node = stack.pop()
#             # 부모 노드 부터 하향식 스왑
#             if node:
#                 node.left, node.right = node.right, node.left
                
#                 stack.append(node.left)
#                 stack.append(node.right)
#         return root
        

        
        