def explosion_string1(s1:str, s2:str) -> str:
    '''
    * 시간초과
    - 첫번째 문자열에 폭발 문자열(2번째 입력) 포함하는 경우,
      첫번째 문자열에 포함된 폭발 문자열 제거,
      남아있는 문자열 반환
    - 첫번째 문자열이 비어있을경우 'FRULA' 반환

    '''
    ans = []
    len_s2 = len(s2)
    for c in s1:        
        ans.append(c)
        if ''.join(ans[-len_s2:]) == s2:
            del ans[-len_s2:]

    if ans:
        return ''.join(ans)
    else:
        return 'FRULA'        

#s1 = '12ab112ab2ab'
#s2 = '12ab' #길이 확인 마지막 

#print(explosion_string1(s1, s2))
print(explosion_string1(s1=input(), s2=input()))