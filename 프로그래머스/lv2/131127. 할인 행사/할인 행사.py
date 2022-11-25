'''
10개씩 슬라이싱
Counter 함수로 같을 때 ans += 1
가능한지 확인
'''
from collections import Counter
def solution(want, number, discount):
    # for k, v in zip(want, number):
    want_dic = {}
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
    
    answer = 0    
    for i in range(len(discount)-10+1):
        cnt = dict(Counter(discount[i:i+10]))
        if want_dic==cnt:
            answer+=1
    
    return answer