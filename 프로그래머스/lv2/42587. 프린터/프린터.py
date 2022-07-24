from collections import deque
def solution(priorities, location):
    '''
    중요도가 높은 문서를 언저 인쇄하는 프린터 개발
    1. 가장 앞에있는 문서(J) 꺼냄
    2. J 이후에 J보다 우선 순위가 하나라도 높은게 있으면 맨 뒤로 보냄
    3. 그렇지 않으면 J 출력
    '''
    ans = 0
    
    idx_prior = deque([(n,i) for i,n in enumerate(priorities)])

    while idx_prior:

        max_val = max(idx_prior)
        tmp_val = idx_prior.popleft()

        if tmp_val[0] == max_val[0]:
            ans += 1
            if tmp_val[1] == location:
                break
        else:
            idx_prior.append(tmp_val)

    return ans