# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev가 있다 -> 비어있음 
        node, prev = head, None
        
        # node가 있는 동안
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev