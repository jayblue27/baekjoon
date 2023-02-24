'''
1. row_begin, row_end 지정
2. 나머지는 col번째 컬럼의 값을 기준으로 오름차순 정렬
3. 
'''

def solution(data, col, row_begin, row_end):
    answer = 0
    # print(data)
    
    # 2번 정렬
    data.sort(key=lambda x:x[0], reverse=True) 
    data.sort(key=lambda x:x[col-1])
    
    # 3번 S_i번째 행의 튜플에 대해 각 컬럼의 값을 i로 나눈 나머지들의 합으로 정의
    B = []
    for i, row in enumerate(data):
        tmp = 0
        for num in row:
            tmp += (num%(i+1))
        B.append(tmp)
    
    # 4번 row_begin 부터 row_end까지 모든 값을 누적하여 XOR 연산
    for i in range(row_begin-1, row_end):
        answer ^= B[i]
        
    return answer