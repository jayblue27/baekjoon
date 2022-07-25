# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 재귀 
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
        
#         # 2. 반복문 - 39ms
#         # 그림 그려서 다시 이해
#         # prev가 있다 -> 비어있음 
#         node, prev = head, None
        
#         # node가 있는 동안
#         while node:
#             next, node.next = node.next, prev
#             prev, node = node, next
            
#         return prev