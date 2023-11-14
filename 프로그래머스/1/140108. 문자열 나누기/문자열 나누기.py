'''
1. 문제이해
- 첫 글자 x의 갯수와 x가 아닌 글자들의 횟수가 같아지는 순간 멈추고, 현재까지의 문자열 분리하고 cnt +=1
- 마지막에 남은건 별도로 하나 +1 (없으면 말고)
- 문자열 분리 -> cnt += 1 

2. 접근방법

- x의 count 값을 담을 변수
- x가 아닌 문자의 count 값을 담을 변수

- for로 s 순환하며
    - x값 지정
    - if c가 x면 x count +=1 
    - x가 아니면 nx count +=1 
    
    - if x count == nx count :
    - answer+=1, x 초기화
    
    - 마지막에 x에 값이 0이 아닌경우 최종값 +1
'''

def solution(s):
    answer = 0
    x_cnt = 0
    nx_cnt = 0
    x = ''
    for c in s:
        if x == '':
            x = c
            
        if c == x:
            x_cnt +=1
        else:
            nx_cnt +=1
        
        if x_cnt != 0 and x_cnt == nx_cnt:
            answer+=1
            x = ''
            x_cnt = 0
            nx_cnt = 0
        
    # 마지막에 남은값 있으면
    if x_cnt != 0:
        answer+=1
    return answer