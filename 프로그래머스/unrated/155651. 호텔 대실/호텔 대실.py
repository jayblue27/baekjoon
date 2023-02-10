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
        time_start = convert_to_mins(start) # 시작 idx
        time_end = convert_to_mins(end)     # 종료 idx
        
        # 시작~종료+10분(청소시간) 까지 1씩 증가
        for i in range(time_start,time_end+10): 
            log_time[i] += 1

    # 최대값 return
    return max(log_time)