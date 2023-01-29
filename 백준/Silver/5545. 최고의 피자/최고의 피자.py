import sys
input = sys.stdin.readline


N = int(input())  # 토핑 수
A, B = map(int,input().split()) # A:도우가격, B:토핑가격
C = int(input()) # C:도우의 열량

ans = 0

#토핑 없는 경우
cal = C 
cost = A
ans = max(cal/cost, ans)

#토핑 칼로리 높은 것 부터 하나씩 늘려가며 최고값 갱신
D = []
for _ in range(N):
    D.append( int(input()) )

D.sort(reverse=True)

for d in D:
    cost += B
    cal += d
    ans = max(cal/cost, ans)
    
    
print(int(ans))