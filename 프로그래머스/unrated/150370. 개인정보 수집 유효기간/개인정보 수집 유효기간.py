from collections import defaultdict

def date_diff(today, date):
    '''날짜 계산하여 month return'''
    today = list(map(int, today.split('.')))
    date = list(map(int, date.split('.')))
    
    y,m,d = today[0] - date[0], today[1] - date[1], today[2] - date[2]
    
    val = y*12 + m + (d*0.01)
    
    return int(val)

def solution(today, terms, privacies):
    result = []
    
    # 약관 딕셔너리 생성
    terms_dic = defaultdict(int)
    for x in terms:
        x = x.split()
        k,v = x[0], x[1]
        terms_dic[k] = int(v)
    
    # 프라이버시 (날짜, 약관) 구분
    pricavies = [x.split() for x in privacies]

    # 본 계산 진행 및 해당 index result에 append
    for i, date in enumerate(privacies, start=1):
        d, t = date.split(' ')

        diff = date_diff(today, d)
        term = terms_dic[t]

        if diff >= term:
            result.append(i)
    
    return result