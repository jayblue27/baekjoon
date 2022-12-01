'''
수확한 귤 중k개 선택
상자 하나에 담아 판매

귤을 크기별로 분류 서로 다른 종류의 수를 최소화 

k개 Counter 써서
len이 가장 짧은 경우 return

생각 잘못 

'''
from collections import Counter

def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    cnt = sorted(cnt.items(), key=lambda x:x[1], reverse=True)

    tmp = []
    
    for key,val in cnt:
        for _ in range(val):
            tmp.append(key)
            
    return len(set(tmp[:k]))
        
    
    
    
    
    
        
        
        
    return answer