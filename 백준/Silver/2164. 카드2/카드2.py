# 백준 - 카드2
# deque 양방향 큐 - 시간복잡도 O(1)
from collections import deque

#입력
N = int(input())
deque = deque([i for i in range(1, N+1)])

# 카드가 1장 남을때 까지 반복한다. 
while len(deque) > 1:
    # 제일 위에 있는 카드를 바닥에 버린다. 
    deque.popleft()
    # 그 다음 제일 위에 있는 카드를 제일 아래로 옮긴다. 
    move_num = deque.popleft()
    deque.append(move_num)

#출력
# 가장 마지막에 남아있는 수 = 덱에 남아있는 수
print(deque[0])