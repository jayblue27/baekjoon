def hanoi(num, start, end, tmp):    
    # 종료 조건 - n이 1개일때는 맨 마지막으로 이동
    if num == 1:                
        print(start, end)
        return 
    # 문제 정의    
    # n-1 개의 원반 모두는 중간 탑을 거치는 과정 필요
    hanoi(num-1, start, tmp, end) 
    print(start, end)    
    # n-1 개의 원반 을 맨 마지막으로 이동
    hanoi(num-1, tmp, end, start)


n = int(input())
print(2**n - 1) #하노이의 탑 최소 이동 횟수 계산식
hanoi(n,1,3,2)