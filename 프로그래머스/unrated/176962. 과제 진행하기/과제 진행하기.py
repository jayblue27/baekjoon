# 모든시간을 분으로 변경
# 시작시간 기준으로 정렬
def solution(plans):
    tmp = []
    done = []
    now = 0
    
    # 시간정보를 분으로 변경
    for plan in plans:
        h, m = map(int, plan[1].split(':'))
        plan[1] = 60*h + m
        plan[2] = int(plan[2])
        
    # 시작시간 기준으로 정렬
    plans.sort(key=lambda x:x[1])
    
    # 
    n = len(plans)
    for i, plan in enumerate(plans):
        sub, s, d = plan

        # 마지막 과목은 무조건 완료
        if i == n-1:
            done.append(sub)
        
        # 마지막 과목 아니면 따져야한다.
        else:
            ns = plans[i+1][1] # 다음시작시간
            term = ns-s        # 다음시작시간까지의 term
            
            if term >= d:      # term이 현재과제 소요시간보다 길거나 같으면
                done.append(sub) # 완료
                term -= d      # term에서 d만큼 빼준다.
                
                if term > 0 and tmp:   # 남은 term이 아직 남아있고 미완list가 남아있으면
                    while term > 0 and tmp:
                        tmp_sub, tmp_d = tmp.pop()
                        if term - tmp_d >= 0: # 미완과제 완료할 여력이 있으면
                            done.append(tmp_sub) # 완료처리하고
                            term -= tmp_d
                        else:                 # 여력 없으면
                            tmp_d -= term     # 남은 시간동안 과제 진행하고
                            tmp.append([tmp_sub, tmp_d])  # 미완과제에 다시 넣고
                            term = 0          # term은 0로 
                            
            else:
                remained = d - term
                tmp.append([sub,remained])
    
    while tmp:
        sub = tmp.pop()[0]
        done.append(sub)
    return done