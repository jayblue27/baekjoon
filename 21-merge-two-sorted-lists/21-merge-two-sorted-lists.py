# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # 내풀이 - TypeError 발생
        # # list가 아닌 연결리스트 형태로 return 해야하는 문제 였음
        # q = []
        # node1, node2 = list1, list2
        # while node1:
        #     q.append(node1.val)
        #     node1 = node1.next
        # while node2:
        #     q.append(node2.val)
        #     node2 = node2.next
        # q.sort()
        # return q
    
        # 책 풀이(재귀) - 34ms
        # l1과 l2값을 비교해 작은 값이 왼쪽에 오게 한다.
        if (not list1) or (list2 and list1.val > list2.val):
            list1, list2 = list2, list1
        # l1 next 를 재귀호출 -> 다음번 연결 리스트가 계속 스왑될 수 있게 한다.
        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)
        return list1

        # 질문 사항
        # 이문제는 어떻게 떠올리는지?
        # 연결리스트 문제가 실제 코테에 나오는지?
        # 다른 해결 방법은 없나?
        
        
            
            
        
        
