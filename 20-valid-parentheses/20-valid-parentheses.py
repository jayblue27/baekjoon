class Solution:
    def isValid(self, s: str) -> bool:
        '''
        string : s -> 괄호 포함
        열린 괄호는 동일한 형태의 닫는 괄호로만 닫을 수 있다.
        모든 괄호가 정상적으로 열고 닫히면 True / 아니면 False return 
        
        ㅇ 접근방법
          - stack에 하나씩 담고 다음 괄호랑 짝을 이루면 pop으로 제거
          - stack에 남은게 없으면 True, 있으면 False
        '''
        stack = []
        brackets = ['()','[]','{}']
        
        stack.append(s[0])
        
        for i in range(1,len(s)):
            stack.append(s[i])
            if ''.join(stack[-2:]) in brackets:
                del stack[-2:]
        
        if stack:
            return False
        else:
            return True
        
            
        