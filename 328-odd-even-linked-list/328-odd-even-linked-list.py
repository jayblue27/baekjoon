# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        홀-짝-홀-짝-홀-짝
        짝으로 시작하면 짝으로 
        '''
        # 풀이 1. 
        # 예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head
        
            
            
        