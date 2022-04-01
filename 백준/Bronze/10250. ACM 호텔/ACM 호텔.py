# 거리 가까운곳 우선 / 층은 숫자 상관 없이 

# 입력
# T : test set 수 (첫줄)

import math 

T = int(input())

tmp = []
for i in range(T):    
    # H : 층 / W : 방 갯수 / N : 손님 수 
    H, W, N = map(int,input().split())
    
    if N%H == 0:
        floors = str(H)
        rooms = str(math.floor(N/H)).zfill(2)
    else:
        floors = str(N%H) 
        rooms = str(math.floor(N/H+1)).zfill(2)

    room_num = floors+rooms
    tmp.append(room_num)

for i in tmp:
    print(i)