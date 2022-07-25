# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        연결리스트 
        매 2개의 인접 노드끼리 스왑 
        '''
        # 1. 값만 교환
        # cur -> head는 왜?
        # head 그대로 두면 안되나?
        cur = head # 인스턴스 생성이구나
        while cur and cur.next:
            #값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next # 2칸씩 움직임
        return head
        
#         # 2. 반복 구조
#         root = prev = ListNode(None)
#         prev.next = head
#         while head and head.next:
#             # b가 a(head)를 가리키도록 할당
#             b = head.next
#             head.next = b.next
#             b.next = head
            
#             # prev가 b를 가리키도록 할당
#             prev.next = b
            
#             # 다음번 비교를 위해 이동
#             head = head.next
#             prev = prev.next.next
#         return root.next
    
#         # 3. 재귀 구조
#         if head and head.next:
#             p = head.next
#             # 스왑된 값 리턴 받음
#             head.next = self.swqpPairs(p.next)
#             p.next = head
#             return p
#         return head
    
    
    
    
        
        