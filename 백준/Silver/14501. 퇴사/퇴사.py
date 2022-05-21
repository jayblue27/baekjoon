#백준 - 퇴사
'''
상담원 백준이 퇴사예정
N+1일째 되는 날 퇴사를 하기 위해 남은 N일 동안 최대한 많은 상담
하루에 하나씩 서로 다른 상담
T는 걸리는 기간, P는 상담료
최대 수익 구하는 프로그램

거꾸로 계산하고 그리디 처럼 max() 써서 최대값 뽑아낸다.
'''
import sys
input = sys.stdin.readline

#입력
N = int(input())
T, P = [0 for i in range(N+1)], [0 for i in range(N+1)]
for i in range(N):
    t,p = map(int, input().split())
    T[i] = t
    P[i] = p


dp =[0] * (N+1)

for i in range(len(T)-2, -1, -1):
    # 날짜를 초과하지 않을 경우.
    if T[i]+i <= N:     
        dp[i] = max(P[i] + dp[i + T[i]], dp[i+1])   
    # 날짜를 초과
    else:                 
        dp[i] = dp[i+1]

print(dp[0])