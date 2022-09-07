'''
레스토랑 
코로나 불경기 극복 위한 메뉴 리뉴얼

단품 only -> 조합을 통한 코스요리
가장 많이 함께 주문한 단품 메뉴들 

최소 2가지 이상 
최소 2명 이상 손님 주문 
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course:
        
        temp = []
        for order in orders:
            combi = combinations(sorted(order), num)
            temp += combi
            
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)