'''
1. 문제이해
- N은 아파트의 수
- stations -> 설치되어있는 기지국 위치
- 5g 기지국을 최소로 설치할 때 기지국의 갯수
- 범위 W * 2 + 1

2. 접근방법
- 1차원 list 생성
- 안테나가 닿는 범위는 1로 지정 그 외에는 0 
- 0이 연속되는 길이 
- W*2+1 로 나눈 몫 올림

3. 오답노트
- N이 2억 시간초과 발생 -> 효율성 전부 실패
- 스트링으로 변환후 정규표현식으로 0갯수 카운트 후 
- 0과 1을 직접 지정할게 아니라 idx만으로 기지국이 닿지 않는 부분을 지정해보자

'''
import math
import re

# def solution(n, stations, w):
#     # 1차원 list 생성
#     apartments = [0] * n
    
#     w_range = w * 2 + 1
#     # 전파도달범위 지정
#     for s in stations:
#         min_idx = max(0, s-w-1)
#         max_idx = min(n, s+w)
        
#         # for i in range(min_idx, max_idx):
#         #     apartments[i] = 1
#         apartments[min_idx:max_idx] = [1] * (max_idx - min_idx)
#     apartments = list(map(str, apartments))
    
#     apartments = ''.join(apartments)
#     matches = re.findall(r'0+', apartments)
#     matches = [len(x) for x in matches]
    
    # max_count = len(max(matches, key=len))
    # print(max_count)
    # 이부분 시간효율성 개선 필요
    # 도달하지 못하는 길이 
#     zero_cnt = 0
#     zero_cnt_list = []
#     for a in apartments:
#         if a == 0:
#             zero_cnt += 1
#         else:
#             if zero_cnt != 0:
#                 zero_cnt_list.append(zero_cnt)
#                 zero_cnt = 0
    
#     if zero_cnt != 0:
#         zero_cnt_list.append(zero_cnt)
    
    
#     # 필요 기지국 수량 카운트
#     zero_cnt_list = [math.ceil(x/w_range) for x in matches]
#     answer = sum(zero_cnt_list)   
        
        
#     return answer

from collections import deque
def solution(n, stations, w):
    idxs = []
    for s in stations:
        s_idx = s-w-1
        e_idx = s+w
        idxs.append(s_idx)
        idxs.append(e_idx)
    # idxs.sort()
#     idxs[0] = 0
#     idxs[-1] = n
    idxs = deque(idxs)
    idxs.appendleft(0)
    idxs.append(n)
    
    zeros = []
    for i in range(0, len(idxs), 2):
        diff = idxs[i+1] - idxs[i]
        if diff != 0:
            zeros.append(diff)
    
    w_range = w * 2 + 1        
    zeros = [math.ceil(x/w_range) for x in zeros]
    answer = sum(zeros)           
    
    return answer