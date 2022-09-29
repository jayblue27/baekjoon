'''
기둥과 보
*기둥 
  - 바닥 위
  - 보의 한쪽 끝 
  - 다른 기둥 위 
*보
  - 한쪽 끝이 기둥 위
  - 양쪽 끝 부분이 다른 보와 동시에 연결
  
작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시

build_frame -> [x,y,a,b]
    - x,y -> 좌표
    - a, 설치 또는 삭제할 구조물의 종류 0 -> 기둥, 1-> 보
    - b, 0 -> 삭제, 1-> 설치
* 바닥에 보를 설치하는 경우 없다.
* 구조물 교차점 좌표 기준 오른쪽, 기둥은 위쪽
* x좌표오름차순, y좌표 오름차순
* x,y 같은 경우 기둥 (0) 이 앞에
'''

def check(answer):
    for x, y, stuff in answer:
        if stuff == 0: #기둥 체크
            #'바닥 위' or '보의 한쪽 끝 위' or '또 다른 기둥 위' 
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        elif stuff == 1: #보 체크
            #'한쪽 끝 부분이 기둥 위' or '양쪽 끝 부분이 다른 보와 동시 연결'
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, stuff, operation = build
        if operation == 1: # 설치
            answer.append([x, y, stuff])
            if not check(answer): answer.remove([x, y, stuff])
        elif operation == 0: # 삭제
            answer.remove([x, y, stuff])
            if not check(answer): answer.append([x, y, stuff])
    answer.sort()
    print(answer)
    return answer
