#백준 A->B - 그리디

# A를 B로 바꾼다. 
# 가능한 연산 2가지
# 1. 2를 곱한다. 
# 2. 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최소값

# 연산수 +1 을 출력하라
# 변환이 안되면 -1을 출력하라

# 거꾸로 생각한다.
# 마지막에 1이 있으면 1을 땐다
# 그외에는 2를 나눈다
# A가 되면 카운트를 반환한다. 
# A보다 작아지면 -1을 반환한다. 

#시간초과 발생 -> 리스트 순회가 문제일까?
import sys
input = sys.stdin.readline
del input
A, B = map(int, input().split())


# 연산수 +1 출력이기 때문에 1부터 시작
cnt = 1
while True:    
    # 종료조건     

    # A랑 같아지면 cnt 출력
    if A == B:
        print(cnt)
        break

    # A를 지나치거나 끝자리가 1 이외의 홀수일때 -1 출력
    elif B < A or (B%10 !=1 and B %2 != 0):
        print(-1)
        break
    

    # 마지막에 1이 있으면 1을 땐다 (type 주의)
    elif B%10 == 1:
        B = B//10
        cnt += 1
    
    # 그외에는 2를 나눈다
    elif B % 2 == 0:
        B = int(B/2)
        cnt += 1