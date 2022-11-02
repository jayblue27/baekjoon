'''
1. 많이 재생된 장르 먼저 수록
2. 장르 내 많이 재생된 순서 수록
3. 장르 내 재생 횟수 같은 노래 고유 번호 낮은 노래

풀이 
- 장르별 재생수 총 합 계산
- 장르별 고유번호 및 재생수 입력 (dic)
- dic 안에서 재생횟수 높은순으로 내림차순 정렬
- 장르별 높은 애들 순서는 어떻게 정하나 -> 리스트로 변환하여 정렬
'''
from collections import defaultdict


def solution(genres, plays):
    #1. dictionary 생성
    dic1 = defaultdict(int) # 장르별 총 재생 수
    dic2 = defaultdict(list) # 곡별 고유번호 및 재생수
    
    for g, t in zip(genres, enumerate(plays)):
        dic1[g] += t[1]
        dic2[g].append(t)
    
    #1번 정렬
    dic1 = list(dic1.items())
    dic1.sort(key=lambda x:x[1], reverse=True)
    
    #2번 정렬
    for k in dic2.keys():
        dic2[k].sort(key=lambda x:x[1], reverse=True)
        
    answer = []
    for tup in dic1: #장르
        genre=tup[0]
        
        for i in range(2):
            if dic2[genre]:
                song = dic2[genre].pop(0)
                answer.append(song[0])
    return answer
    
    

    #     dic1 = {} # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
#     dic2 = {} # {'classic': 1450, 'pop': 3100}

#     # enumerate + zip 
#     # 딕셔너리 생성
#     for i, (g, p) in enumerate(zip(genres, plays)):
#         if g not in dic1:
#             dic1[g] = [(i, p)]
#         else:
#             dic1[g].append((i, p))

#         if g not in dic2:
#             dic2[g] = p
#         else:
#             dic2[g] += p
    
#     # 정렬해서 뽑기 
#     for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
#         for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
#             answer.append(i)

#     return answer