class Solution:
    def isValid(self, s: str) -> bool:
        '''
        string : s -> 괄호 포함
        열린 괄호는 동일한 형태의 닫는 괄호로만 닫을 수 있다.
        모든 괄호가 정상적으로 열고 닫히면 True / 아니면 False return 
        
        ㅇ 접근방법
          - stack에 하나씩 담고 마지막 두개가 brackets안의 형태를 띄면 원소 삭제
          - stack에 남은게 없으면 True, 있으면 False
        '''
        # 내 풀이 - 41-44ms
        
        stack = []
        brackets = ['()','[]','{}']
        
        # 하나씩 stack에 입력
        for c in s:
            stack.append(c)
            # stack의 마지막 2개가 brackets 안의 형태와 같으면 제거
            if ''.join(stack[-2:]) in brackets:
                del stack[-2:]
        
        # 남은 원소 없으면 True / 있으면 False
        if stack:
            return False
        else:
            return True
        
#         # 책 풀이 - 딕셔너리 사용,  51-59ms
#         # 딕셔너리 써러 더 시간이 빠를 줄 알았는데
#         stack = []
#         table = {
#             ')':'(',
#             '}':'{',
#             ']':'['
#             }
        
#         for c in s: # O(n)
#             if c not in table: # O(n)
#                 stack.append(c)
#             elif not stack or table[c] != stack.pop():
#                 return False
#         return len(stack) == 0
        
            
        