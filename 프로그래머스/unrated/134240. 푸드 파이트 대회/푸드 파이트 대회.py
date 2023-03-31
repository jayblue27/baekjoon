'''
매달 푸드파이트 대회
양쪽에서 먹기시작하고 중앙에 물 먼저 먹는 선수 승리

food[0]은 항상 0

2로 나눈 몫을 가지고
정방향, 역방향 str 만든다음

정방향 + 0 + 역방향 
'''

def solution(food):
    answer = ''
    for i, f in enumerate(food):
        answer += str(i) * (f//2)
        # print(i)
    rev = answer[::-1]
    answer += str(0) + rev
    return answer