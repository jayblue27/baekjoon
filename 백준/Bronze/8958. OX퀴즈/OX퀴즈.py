# 카운트 2개 써서 하면 될 듯
# O가 연속

#Input
#첫째 줄 케이스 갯수
n = int(input())

#두번째 줄부터 케이스 입력 (한 줄에 하나)
cases = []
for i in range(n):
    case = input()
    cases.append(case)


# Output
# 전체 케이스 순회
for case in cases:
    count_sum = 0 # 총 점수    
    m_count = 0    
    s_count = 0

    # 케이스내부 순회
    for point in case:             
        if point == 'O':  # O 나오면 
            s_count += 1  # sub count는 1씩 올라감 연속점수
            m_count += s_count  # m count 는 연속점수를 더해줌
        else:            
            s_count = 0  # x 나오면 초기화
            
        
    print(m_count)  # 최종 점수 출력( 1줄마다)
