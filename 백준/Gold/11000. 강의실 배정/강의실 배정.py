# 강의실 배정
'''
S에 시작해서 T에 끝나는 N개의 수업 
최소의 강의실을 사용해서 모든 수업이 가능해야 함

N : 수업수 (1 <= N <= 200,000)
S,T : 시작시간, 종료시간
'''
import heapq
import sys
input = sys.stdin.readline

#입력
N = int(input())
classes = [] #수업시간표
for _ in range(N):
    S,T = map(int, input().split())
    classes.append([S,T])
classes.sort(key=lambda x:x[0]) #정렬

#종료시간 큐에 담는다. 
q = []
heapq.heappush(q,classes[0][1])

for i in range(1,N):
    # 앞시간 수업이 아직 안끝났을 때 신규로 push
    if q[0] > classes[i][0]:
        heapq.heappush(q,classes[i][1])
    # 수업이 끝나면 q에서 제거하고 새로운 수업 을 넣는다.
    else:
        heapq.heappop(q)
        heapq.heappush(q,classes[i][1])
print(len(q))

#힙큐는 최솟값(혹은 최댓값)을 계속 뽑을때 사용한다. 
#값들이 계속 추가 되는경우 리스트는 매번 정렬을 해줘야 하기 때문에
#heapq를 쓰면 시간 복잡도를 줄일 수 있다. 