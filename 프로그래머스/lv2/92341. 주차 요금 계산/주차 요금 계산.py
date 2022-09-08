'''
1. 특정 차량 번호에 대한 주차 시간을 담을 딕셔너리 정의
2. 시간, 차량번호, 입/출차 정보 구분 처리

'''

import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    
    dict = {}
    parking_info = defaultdict(int)

    # 주차한 시간
    for record in records :
        time, number, state = record.split() # 시간, 차량 번호, 입/출차 정보 구분

        # 시간
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            # print(dict,parking_info)
            parking_info[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time
    
    # 출차를 안 한 경우
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        parking_info[num] += max_time - t

    # 요금 계산
    basic_minutes, basic_fee, split_minutes, split_fee = fees
    for num, t in parking_info.items() :
        cost = basic_fee
        if t > basic_minutes : # 추가 요금 발생
            cost += math.ceil((t - basic_minutes) / split_minutes) * split_fee # 올림 처리
        answer.append((num, cost))

    # 차량 번호 오름차순
    answer.sort()
    return [value[1] for value in answer]