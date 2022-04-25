# S를 알때? N개의 최대값
# N이 늘어나려면 작은 숫자부터 더해야
# 근데 200이 되는 숫자를 어떻게 알아내냐? 
# 문제 이해하는데 시간이 조금 걸렸다.

S = int(input())

tmp = 0 # 임시 저장 변수 
num = 1 # num
cnt = 0 # count
# while로 1부터 순차적으로 더하고
while True:
    tmp += num         
    num += 1
    
    # S값을 넘기면 cnt를 반환하면 된다. 
    if tmp > S:
        print(cnt)
        break
    
    cnt += 1