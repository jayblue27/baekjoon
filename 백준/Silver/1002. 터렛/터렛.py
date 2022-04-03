#입력
# N 회 
# x1, y1, r1, x2, y2, r2
# x, y -> -10000~ 10000
# r -> 0~ 10000

import math

N = int(input())

tmp = []
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt( math.pow(x1-x2, 2) + math.pow(y1-y2, 2) )  # 원의 방정식 두 원의 거리

# 출력
# 적군이 있을 수 있는 위치의 수 두개의 원이 겹치는 
# 원 두개 그려서 겹치는 수 구나
# 완전히 겹치면 -1 반환
    
    # 위치가 똑같고, 반지름이 같을 때 (무한대)
    if dist == 0 and r1 == r2: 
        tmp.append(-1)
    #내접 : 두점의 거리 == 두 원 반지름 차이
    #외접 : 두점의 거리 == 두 원 반지름 합
    elif abs(r1-r2) == dist or r1 + r2 == dist: 
        tmp.append(1)
    # 2점이 겹칠 때
    elif abs(r1-r2) < dist < abs(r1+r2):
        tmp.append(2)
    # 그 외에는 겹치는 점 없음
    else:
        tmp.append(0)

for i in tmp:
    print(i) 