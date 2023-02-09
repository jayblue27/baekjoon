# def solution(book_time):
#     answer = 0
#     return answer


"""
- 문제풀이
부분합(누적합)
시작시간부터 종료시간까지 1씩 더해준다. 
log 시간의 max값 return 
"""

def convert_to_mins(time):
    '''문자형태로 주어진 시간을 분으로 변경'''
    h, m = time.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    # 시간을 분으로 바꿔서 
    # 누적합 이용 최대 값을 return
        
    # 1. 전체 분을 배열로 담기 (누적합을 위한)
    log_time = [0] * ((24*60)+10)

    # 2. 모든 시간을 분으로로 변환
    for start, end in book_time:
        time_start = convert_to_mins(start) # 동영상 재생시간
        time_end = convert_to_mins(end)   # 공익광고 재생시간
        
        for i in range(time_start,time_end+10):
            log_time[i] += 1

    return max(log_time)
    