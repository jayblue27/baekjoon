"""
- 문제풀이
부분합(누적합)
각 시청기록의 시작과 종료를 찾고

광고길이만큼의 윈도우를 슬라이딩 하며
누적합이 가장 큰 index(시작초)를 찾아서
string 형태의 시간으로 바꿔준다.
"""

def convert_to_seconds(time):
    '''시간을 초로 변경'''
    h, m, s = time.split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)

def solution(play_time, adv_time, logs):
    # 1. 모든 시간을 초로 변환
    play_time = convert_to_seconds(play_time) # 동영상 재생시간
    adv_time = convert_to_seconds(adv_time)   # 공익광고 재생시간

    # 2. 전체 초를 배열로 담기 (누적합을 위한)
    log_time = [0 for _ in range(play_time + 1)]
    
    for log in logs:
        # 로그(시청기록)의 시작과 끝 -> 초로 변환
        start, end = log.split('-')
        start = convert_to_seconds(start)
        end = convert_to_seconds(end)
        # 각 로그의 시작(1)과 종료(-1) 표기
        log_time[start] += 1
        log_time[end] -= 1
    
    # 2. 전체 초별로 누적 시청자 수 구하기 (직전의 index와의 합을 구하기)
    for i in range(1, len(log_time)):
        log_time[i] += log_time[i - 1]
    
    # 3. 광고시간만큼의 윈도우 생성
    window_sum = sum(log_time[:adv_time]) # 최초의 구간합
    max_sum = window_sum
    max_idx = 0
    
    # 4. 슬라이딩 윈도우 시작
    for i in range(adv_time, play_time):
        # 기존의 값(window_sum)에
        # log_time[i] 새로운 값을 더하고, log_time[i-adv_time] 맨 앞의 값을 빼주면서 구간합 계산
        window_sum = window_sum + log_time[i] - log_time[i-adv_time] 
        # 최대 구간합 갱신 및 최대 구간합의 index 계산
        if window_sum > max_sum:
            max_sum = window_sum
            max_idx = i-adv_time + 1
    
    # 5. 위에서 구한 max_idx(광고효과가 가장 좋은 시작 시간(초))를 문자열 시간 형태로 변환 하여 반환 
    m, s = divmod(max_idx, 60)
    h, m = divmod(m, 60)
    
    return f'{h:02d}:{m:02d}:{s:02d}'
    
    

