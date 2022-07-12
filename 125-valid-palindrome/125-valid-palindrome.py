class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        ㅇ 팰린드롬(회문)이란? 
          - 앞으로 읽으나 뒤로 읽으나 똑같은 알파벳 혹은 숫자(alphanumeric)
          
        
        ㅇ 풀이 접근법
          - s 변환 : 소문자로 변경, 알파벳/숫자 제외한 문자 제거
            -> .isalpha() or .isnumeric() / .isalnum() 중 적절히 사용
          
          - s 와 뒤집힌 s가 같을 경우 true(1) / 다를경우 false(0) 출력
        '''
        
        new_s = ''
        
        # .isalnum() 이용 문장(s) 안의 문자열이 문자 혹은 숫자 인지 확인        
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        
        if new_s == ''.join(reversed(new_s)):
            return 1
        else:
            return 0
        
            
        