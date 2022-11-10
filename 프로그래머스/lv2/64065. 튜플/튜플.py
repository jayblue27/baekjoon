'''
n개의 요소가진 tuple -> n-튜플

튜플을 표현하는 문자열s
s가 표현하는 튜플을 배열(리스트)에 담아 return

궁금증 return하는 result 순서는 상관없는건가? 

- 문자열을 리스트 형태로 바꾸자
    - 가장 외곽의 괄호 제거
    
- 원소 개수대로 정렬해서
- 처음 나오는 애부터 result에 입력 한다.
- 새로 들어오는 원소가 이미 result에 있는 경우 무시 없는 경우에만 result에 추가

'''

import re
def solution(s):
            
    pattern = r'{[0-9\,]+}'
    s = re.findall(pattern, s)
    s = [c.lstrip('{') for c in s]
    s = [c.rstrip('}') for c in s]
    s = [c.split(',') for c in s]
    s.sort(key = lambda x:len(x))
    
    answer = []
    for arr in s:
        for num in arr:
            if num not in answer:
                answer.append(num)
        
    answer = list(map(int,answer))
    return answer

    
    #     answer = []
#     tmp = []
#     for i in range(1, len(s)):
#         tmp.append(s[i])
    
    # return answer