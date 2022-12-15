'''
point : C#->c 소문자로 변경하여 처리가 쉽게 만들어줬다.(길이 비교가 어려움)

재생시간 확인
기억한 음(m)이 음악에 있는지 확인 
음이 중간에 끊겼는지 확인
'''
sharp = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}

def sharp_to_lower(m):
    '''#이 포함된 음을 소문자 음계로 바꿔 길이를 동일하게 유지시켜준다.'''
    for s in sharp.keys():
        m = m.replace(s, sharp[s])
    return m

def time_to_min(time):
    '''문자열 시:분을 int 분으로 통일하여 반환'''
    h, m = map(int,time.split(':'))
    return h * 60 + m
    
def play_music(code, duration):
    '''code와 재생시간을 받아 전체 재생시간동안의 코드진행을 문자열로 return'''
    code = sharp_to_lower(code)
    # 반복 횟수만큼 반복해서 return 
    code = code * (duration // len(code) +1) # code * 반복횟수
    return code[:duration] #실행된 분 만큼 잘라줌
    
def solution(m, musicinfos):
    answer = None
    m = sharp_to_lower(m)
    
    hist = []
    for music in musicinfos:
        # 정보 확인
        start, end, title, code = music.split(",")
        
        # 재생 시간(분)확인   (종료분 - 시작분)   
        duration = time_to_min(end) - time_to_min(start)
        # print(duration)
        
        # 기억한 음(m)이 전체 재생한 코드 진행에 있던 음인지 확인
        code = play_music(code, duration) 
        if m in code:
            hist.append((title,duration))
    hist.sort(key=lambda x:x[1], reverse=True)
    if hist: return hist[0][0]
    return '(None)'
        
