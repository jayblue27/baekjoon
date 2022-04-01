# 입력
N = int(input())

line = 0  # 사선 라인 순서
max_seq_num = 0  # 입력된 숫자(N 변수)의 대각선 라인(순서)에서 가장 큰 순서
while N > max_seq_num:     # max_seq_num이 입력된 정수보다 작으면 계속 돌린다.
    line += 1                    
    max_seq_num += line    # line의 원소 갯수는 line의 숫자와 같음, seq는 1 -> 3(1+2) -> 6(1+2+3) ...    

gap = max_seq_num - N  # 몇 번째 시퀀스에 위치하는지 확인 위한 gap
from_big = line-gap #line이 가장 큰 숫자이니, line에서 움직인 칸수(gqp) 만큼 이동
from_small = gap + 1 # 시작번호가 1이니 gqp이 0일 경우(시작점 일경우) +1 해준다.

# 짝수면 분자가 큰수 -> 작은수
if line % 2 == 0:  # 사선 라인이 짝수번째 일 때     
    print(f'{from_big}/{from_small}')

# 홀수면 분자가 작은수 -> 큰수
else :  # 사선 라인이 홀수번째 일 때
    print(f'{from_small}/{from_big}')