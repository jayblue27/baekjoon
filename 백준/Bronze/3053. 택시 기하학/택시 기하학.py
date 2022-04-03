import math

# 입력
# r : 반지름
r = int(input())

# 출력
# 원의 넓이

print(format(math.pi * math.pow(r,2), ".6f") ) # 유클리드 pi * r^2
print(format(math.pow(r,2) * 0.5 * 4, ".6f") )  # 택시 기하학 직각삼각형 4개 -> r^2 * 1/2

# 배울점 : 소수점 고정 출력
#format(변수, ".5f")