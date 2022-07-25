# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         # 1. 파이썬 리스트로 변환 - 1773 - 2569ms
#         q = []  # 큐 선언
            
#         # 비어있는것도 팰린드롬이기 때문에 'True' return
#         if not head:
#             print(node)
#             return True
        
#         #첫 노드 선언
#         node = head
#         # 리스트 변환
#         while node is not None: # O(n), 모든 노드 순환
#             q.append(node.val) # q에 현재 값 넣어주고 
#             node = node.next   # 다음 노드로 지정
#         #팰린드롬 판별 - O(n^2) - while * pop(0)
#         # 처음과 끝 원소 하나씩 pop 하면서 비교하고 다를 경우 return False 
#         while len(q) > 1: # O(n)
            
#             if q.pop(0) != q.pop(): #pop(0) -> O(n) * O(1) <- pop()
#                 return False
#         return True # 원소 1개 남았을때 True 리턴
        
#         # 2. deque - 942-1434ms
#         # 1번과 판별부분 pop(0) 를 popleft() 로 바꿔준거 밖에 없는데 시간이 많이 줄어든다. 
#         q = collections.deque()
#         if not head:
#             return True
        
#         node = head
#         # 리스트 변환
#         while node is not None: # O(n)
#             q.append(node.val)
#             node = node.next
#         #팰린드롬 판별
#         while len(q) > 1: # O(n)
#             if q.popleft() != q.pop():  # popleft -> O(1)
#                 return False
#         return True 
            
        # 3. 런너(?) 이용 - 694ms, 아직 이해가 어렵다. 
        rev = None # rev?
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast: # fast 다음이 none이면 더이상 움직일 곳이 없다.
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
        