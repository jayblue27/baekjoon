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
        #풀이 1 - 재귀 구조 DFS로 부르트포스 탐색 - 492ms 
        if not root:
            return 0
        
        return (root.val if low <= root.val <= high else 0) + \
                self.rangeSumBST(root.left, low, high) + \
                self.rangeSumBST(root.right, low, high)
    
        #풀이 2 - DFS 가지치기로 필요한 노드 탐색
        def dfs(node: TreeNode):
            if not node:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        return dfs(root)
        
        #풀이 3 - 반복부조 DFS로 필요한 노드 탐색
        stack,sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
    
        #풀이 4 - 반복 구조 BFS로 필요한 노드 탐색
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
                if low <= node.val <= high:
                    sum += node.val
        return sum
        