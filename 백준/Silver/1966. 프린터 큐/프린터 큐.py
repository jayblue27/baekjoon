#백준 - 프린터 큐
#덱을써서 leftpop한 숫자를 append 순환 시킨다. 
#우선
from collections import deque 

# 테스트 케이스 
T = int(input()) 

# 케이스만큼 반복
for _ in range(T):
    # N개의 문서, M번째 정수
    N, M = map(int,input().split())    
    # 문서 입력    
    que = deque(list ( map(int, input().split()) ) )      
    idx_que = deque(list(range(N))) #인덱스 큐 선언
    
    # 우선순위를 담기위한 cnt
    cnt = 0 
    # 문서를 순회하며
    while que:
        # 문서의 첫번째가 가장 큰 값이면 
        if que[0] == max(que):
            #cnt 하나 올리고 
            cnt += 1
            #문서출력
            que.popleft()
            if idx_que.popleft() == M:
                print(cnt)
        else:
            # 문서랑, 순서 popleft해서 바로 append - 맨끝으로 보내기
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())
    