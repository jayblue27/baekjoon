'''
1. 많이 재생된 장르 먼저 수록
2. 장르 내 많이 재생된 순서 수록
3. 장르 내 재생 횟수 같은 노래 고유 번호 낮은 노래

'''
def solution(genres, plays):
    answer = []

    dic1 = {} # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    dic2 = {} # {'classic': 1450, 'pop': 3100}

    # enumerate + zip 
    # 딕셔너리 생성
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    
    # 정렬해서 뽑기 
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer