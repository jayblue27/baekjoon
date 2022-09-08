from collections import defaultdict

def solution(id_list, report, k):
    
    answer = [0] * len(id_list) # id_list 길이에 맞는 정답 리스트 생성 값은 0
    
    # 한 유저가 같은 유저를 여러번 신고한 경우는 신고 횟수 1회로처리 하기 때문에 set로 중복값을 제거
    # 주어지는 report 리스트를 중복 제거 해주는 것이 이 문제의 핵심이었다.
    # 이 한줄의 코드 없이 제출하면 시간초과 발생 
    report = set(report) 

    user_list_who_i_report = defaultdict(set) # value값이 set를 가지는 dict 생성
    num_of_reported = defaultdict(int) # 몇번 신고 당했는지 기록하는 dict 생성(int)
        
    suspended = []  # 정지 id 리스트

    for r in report: 
        do_report, be_reported = r.split() # 신고자, 피신고자 분리
        
        num_of_reported[be_reported] += 1  # 신고 당하면 피신고자 value 1씩 증가
        user_list_who_i_report[do_report].add(be_reported) # 신고자가 누구를 신고했는지 key-value
        
        if num_of_reported[be_reported] == k: # k회 도달하면 정지 리스트에 추가
            suspended.append(be_reported)

    for s in suspended:  
        for i in range(len(id_list)): 
            if s in user_list_who_i_report[id_list[i]]: # 신고자가 정지리스트에 오르면
                answer[i] += 1  # 메일 받은 횟수 1씩 증가 # 해당 인덱스에 증가
    
    return answer