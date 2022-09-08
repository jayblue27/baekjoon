'''
규칙1 : 최소 2가지 이상의 단품메뉴
규칙2 : 최소 2명 이상의 손님으로부터 주문된 단품 메뉴
규칙3 : 가장 많이 주문된 조합

오름차순 정렬
메뉴 구성이 여러 개라면 모두 배열에 담는다.
'''

from itertools import combinations
from collections import Counter

# orders : 단품 메뉴 종류
# course : 메뉴 구성 수
def solution(orders, course):
    answer = []
    
    for num in course:
        temp = []
        
        for order in orders:
            combi = combinations(sorted(order), num)            
            temp += combi
                
        counter = Counter(temp)
        print(counter)
        
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)