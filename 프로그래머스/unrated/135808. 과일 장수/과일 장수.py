'''
과일장수 사과포장
k점 -> 최상
1점 -> 최하

한 상자에 사과 m개씩 

k점 
m개
p 가장 낮은 점수
-> p*m이 상자 가격
score -> 사과들의 점수 

최대 이익 ?
이익 발생하지 않는 경우 0 

큰수부터 잘라서 
'''

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    return answer