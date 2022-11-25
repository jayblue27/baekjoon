'''
I -> answer.append()

D -> answer 오름차순 정렬
    1 -> 마지막 수(최대값) pop
    -1 -> 첫번째 수(최소값) pop
'''

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
            
        print(op, answer)
            
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]
            
            
    
    
    
    return answer