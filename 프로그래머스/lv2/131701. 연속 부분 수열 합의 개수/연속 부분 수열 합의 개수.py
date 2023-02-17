'''
월형 수열
중복제거 - set, dict(key)
elements 길이 뽑아두고
elements * 2배 해서 순환 가능하게 하고 
set에 값을 넣어주자
'''

def solution(elements):
    arr = []
    
    n = len(elements)
    elements = elements * 2
    
    for i in range(n):
        for j in range(n):
            arr.append(sum(elements[i:i+j]))        
    
    return len(set(arr))