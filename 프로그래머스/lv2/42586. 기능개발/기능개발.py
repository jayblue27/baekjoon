# '''
# progresses가 100% 일 때 서비스에 반영가능
# 빠른 기능이 먼저 완료되어야 한다.

# 1. 프로그레스를 100에서 뺀 값으로 바꿔주고
# 2. 그 값을 speeds 몫 연산자로 
# '''
# def solution(progresses, speeds):
#     answer = []    
#     return answer






# 프로그래머스 - 기능개발 
def solution(progresses, speeds):
    answer = []
    while progresses:
        # 프로그레스 진행 시키는 부분
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 첫번째 기능의 진행률이 100 넘으면 배포
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

solution(progresses, speeds)