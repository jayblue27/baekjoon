# A -> B 아기기스 군사기지 융단폭격
# B나라 요격 최소의 미사일
# s,e 에서는 요격할 수 없고 
# 실수좌표 x에서 발사 가능


def solution(targets):
    targets.sort(key=lambda x: x[1])  # 각 개구간의 끝 위치를 기준으로 정렬
    # print(targets)
    cnt = 1
    cur_end = targets[0][1]
    # print(cur_end)
    for s, e in targets:
        if cur_end > s:  # 이전에 처리된 개구간과 겹치지 않는 경우
            continue
        else:
            cnt+=1
            cur_end = e
    return cnt