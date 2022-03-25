#Input
A, B, C = map(int, input().split())

#cond. 1
# 같은 눈이 3개 나오면 10000원 + (숫자 x 1000)
if A == B and B == C and A == C:
    print(10000 + (A*1000) )

#cond. 2
# 같은 눈이 2개만 나오면 1000원 + (숫자 x 100)
elif A==B or A==C:
    print(1000 + (A*100) )
elif B==C:
    print(1000 + (B*100) )

#cond. 3
#모두 다른 눈이 나오는 경우 (가장 큰 숫자) x 100
else:
    print(max(A,B,C) * 100)