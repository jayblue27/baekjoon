'''
개발언어 - cpp,java,python 중 하나
직군 - backend, frontend 
경력 - junior, senior 
소울푸드 - chicken, pizza

'''

# from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left

# def solution(information, queries):
#     answer = []
#     dic = defaultdict(list)
#     for info in information:
#         info = info.split()
#         condition = info[:-1]  
#         score = int(info[-1])
#         for i in range(5):
#             case = list(combinations([0,1,2,3], i))
#             for c in case:
#                 tmp = condition.copy()
#                 for idx in c:
#                     tmp[idx] = "-"
#                 key = ''.join(tmp)
#                 dic[key].append(score) 

#     for value in dic.values():
#         value.sort()   

#     for query in queries:
#         query = query.replace("and ", "")
#         query = query.split()
#         target_key = ''.join(query[:-1])
#         target_score = int(query[-1])
#         count = 0
#         if target_key in dic:
#             target_list = dic[target_key]
#             idx = bisect_left(target_list, target_score)
#             count = len(target_list) - idx
#         answer.append(count)      
#     return answer

# 모든 경우에 대해서 tree형태로 생각할 수 있다.
# 언어 4가지 * 직군 3가지 * 경력 3가지 * 소울푸드 3가지 = 108가지 
# 4차원 배열로 표현하거나, 모든 경우에 대해서 1차원 배열로 표현 가능함
from bisect import bisect_left

def solution(info, query):
    wmap = {'-':0, 'cpp':1, 'java':2, 'python':3,
                    'backend':1, 'frontend':2,
                    'junior':1, 'senior':2,
                    'chicken':1, 'pizza':2}
    slist = [[] for _ in range(4*3*3*3)]
    
    for string in info:
        w = string.split()
        arr = (wmap[w[0]]*3*3*3,    #언어
              wmap[w[1]]*3*3,       #직군
              wmap[w[2]]*3,         #경력
              wmap[w[3]])           #소울푸드
        score = int(w[4])           # 점수
        
        for i in range(1<<4): # 쿼리 항목이 4개 1을 왼쪽으로 4번  00001 -> 10000(16)   i 값 : 0~15번 까지
            idx = 0
            for j in range(4):
                if i & (1 << j):  # j번째 원소가 있는 경우 
                    idx += arr[j]
            slist[idx].append(score)
    
    for i in range(4*3*3*3):
        slist[i] = sorted(slist[i])
    
        
    answer = []
    for string in query:
        w = string.split()
        idx = wmap[w[0]]*3*3*3 + wmap[w[2]]*3*3 + wmap[w[4]]*3 + wmap[w[6]]
        score = int(w[7]) 
        answer.append(len(slist[idx]) - bisect_left(slist[idx], score)) 
        # bisect_left  ex) [100, 200, 300] 50을 추가시 0번째 인덱스에 넣어야 한다 
        # score(50) 보다 큰 사람이 원래 리스트 길이(3) - index(0) = 3 명 
        # score(250) 보다 큰 사람이 원래 리스트 길이(3) - index(2) = 1 명
    
    return answer