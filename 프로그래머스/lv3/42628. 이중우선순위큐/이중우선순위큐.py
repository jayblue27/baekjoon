
def solution(operations):
    answer = []
    for op in operations:
        k, v = op.split()
        if k =='I':
            answer.append(int(v))
        
        answer.sort()
        if answer and k =='D' and v == '1':
            answer.pop()
        if answer and k =='D' and v == '-1':
            answer.pop(0)
            
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]
            
            
    
    
    
    return answer