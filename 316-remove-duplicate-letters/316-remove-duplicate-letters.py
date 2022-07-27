class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        문자열 s 주어짐
        중복문자 제거하고 사전 오름차순 형태로(?)
        
        문자
        ㅇ 나의 접근방법
        1. 문자열 -> sorted(문자열) 로 리스트화
        2. 리스트 -> set() 로 중복 제거
        3. str()로 문자열로 다시 돌리기
        '''
        # # 내풀이(틀림)  - 예제 1번은 맞는데, 예제 2번이 틀림 
        # # 문제 이해를 제대로 하지 못함(정렬의 순서)
        # s = ''.join(sorted(list(set(s))))
        # return s
        
        # 책풀이 2(스택)
        counter, seen, stack = collections.Counter(s), set(), []
        
        # 문자열 순환하면서
        for c in s:
            # counter의 값을 하나씩 줄여간다
            counter[c] -= 1
            
            # 이미 seen 집합에 문자열이 들어있으면
            if c in seen:
                continue # 아래 생략
                
            # 뒤에 붙일 문자가 남아 있다면
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop()) # seen에서 해당 문자 제거 해준다. 알파벳 하나하나씩 체크해서 그런거 (2단어씩 하는게 아님)
            stack.append(c)
            seen.add(c)
        return ''.join(stack)
        
        
        

        