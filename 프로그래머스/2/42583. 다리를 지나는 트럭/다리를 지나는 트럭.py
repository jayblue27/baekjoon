'''
16시 35분 시작

1. 문제이해
- 동시에 bridge_legnth 대 만큼 다리위에 차가 올라갈 수 있음
- 동시에 weight 무게만큼 다리위에 차가 올라갈 수 있음
- 길이 1씩 움직일때마다 1초씩 증가 


2. 문제접근
- 다리 = stack 
- while 로 
- 하나씩 

'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    truck_bridge_deque = deque(bridge_length * [0])
    truck_weights_deque = deque(truck_weights)
    
    while truck_bridge_deque:
        answer += 1
        temp -= truck_bridge_deque[0]
        truck_bridge_deque.popleft()
        if truck_weights_deque:
            if temp + truck_weights_deque[0] <= weight:
                temp += truck_weights_deque[0]
                truck_bridge_deque.append(truck_weights_deque.popleft())
            else:
                truck_bridge_deque.append(0)
    return answer