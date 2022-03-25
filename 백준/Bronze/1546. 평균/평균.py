# Input
# 1. 시험 과목수 (int)
# n = int(input("시험 과목 수: "))
n = int(input())

# 2. 과목별 점수 (1번개)
# n개의 변수를 어떻게 지정? 수평으로
# 일단 수직으로 구현하기 
# list 함수를 썼다
# x = list(map(int, input("과목별 점수: ").split()))
x = list(map(int, input().split()))


# Output
# M : 과목중 최대값
# 과목별 점수/ M * 100
# 새로운 점수 평균 계산

M = max(x)
res = [(i/M*100) for i in x]
print(sum(res)/n)