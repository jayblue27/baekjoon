# 완호의 점수(scores[0]) 고과등수 확인
# 두 점수 합이 같으면 동점 
# ! 제거할사람을 찾으려고 전체순환하면 시간초과 n^2
# 

# def solution(scores):
#     answer = 0 
#     wanho = scores[0]
#     # 순환하면서

#     for a,b in scores:
#         # 완호가 인센티브 받지 못하는 경우
#         if a > wanho[0] and b > wanho[1]:
#             return -1
    
    
    
#     return answer

def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    threshold = 0
    for score in scores:
        # 완호가 못받는 경우 
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        
        if threshold <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            threshold = score[1]
    return answer