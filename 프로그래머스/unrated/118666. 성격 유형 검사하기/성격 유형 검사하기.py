'''
성격유형 검사지
1번 RT 
2번 CF
3번 JM
4번 AN

평가 list 만들고
점수 만들고



동점일때는 RCJA (알파벳이 빠른 순)

딕셔너리 만들고

choices의 값이 4보다 작으면 앞의 항목에 4를 뺀 절대값을 넣어준다.
항목별로 비교후 answer에 값을 넣어준다.
'''
def solution(survey, choices):
    # 딕셔너리 만들고 
    score_table = {'R':0, 'T':0,
                   'C':0, 'F':0,
                   'J':0, 'M':0,
                   'A':0, 'N':0}
    
    
    for s, c in zip(survey, choices):
        s_list = list(s)
        if c < 4:
            score_table[s_list[0]] += abs(c-4)
        else:
            score_table[s_list[1]] += abs(c-4)
    
    answer = ''
    test_list = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i,j in test_list:
        if score_table[i] < score_table[j]:
            answer+=j
        else:
            answer+=i
    
    return answer