# 백준 - 회전하는 큐 
'''
회전하는 큐
1. 첫번째 원소 제거
2. 왼쪽으로 한칸 이동
3. 오른쪽으로 한칸 이동

#입력
N : 큐의 크기, M 뽑아내려고 하는 수의 개수
'''

from collections import deque

N,M=map(int,input().split())
lst=deque(range(1,N+1))
q=deque(map(int,input().split()))

cnt=0
#큐 있을때
while q:    
    # 중간 설정하고 
    mid=len(lst)//2
    # 중간보다 크면 오른쪽으로 순환
    if lst.index(q[0])>mid:
        # 첫번째 원소가 같아질때
        while q[0]!=lst[0]:
            lst.appendleft(lst.pop())
            cnt+=1
        lst.popleft()
        q.popleft()
    # 중간보다 작으면 왼쪽으로 순환
    else:
        while q[0]!=lst[0]:
            lst.append(lst.popleft())
            cnt+=1
        lst.popleft()
        q.popleft()
print(cnt)