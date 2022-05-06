#백준 - 프린터 큐
from collections import deque 

# 테스트 케이스 
T = int(input()) 

# 케이스만큼 반복
for _ in range(T):
    # N개의 문서, M번째 정수
    N , M = map(int,input().split())    
    # 문서 입력
    que = deque(list(map(int,input().split())))
    # 인데스 큐는 왜?
    idx_que = deque(list(range(N)))
    
    
    cnt = 0 
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx_que.popleft() == M:
                print(cnt)
        else:
            que.append(que.popleft())
            idx_que.append(idx_que.popleft())