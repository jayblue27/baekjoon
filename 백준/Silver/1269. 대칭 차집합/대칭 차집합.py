# 대칭 차집합 - 실버 4
'''
두 집합 A,B 
대칭 차집합 원소의 개수 
set처리
A-B, B-A의 길이를 더한 값 출력
'''
nA, nB = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))

print(len(A-B) + len(B-A))