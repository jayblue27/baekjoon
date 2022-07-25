# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. 파이썬 리스트로 변환 - 2569ms
        q = []
        
        if not head:
            return True
        
        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next
        #팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
#         # 2. deque - 942-1434ms
#         q = collections.deque()
#         if not head:
#             return True
        
#         node = head
#         # 리스트 변환
#         while node is not None:
#             q.append(node.val)
#             node = node.next
#         #팰린드롬 판별
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
        
        
        
        
        
        
        return True
        
        