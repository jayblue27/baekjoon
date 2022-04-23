#numpy 쓰면 런타임에러 발생
# import numpy as np
# print(np.dot(A,C))
#입력
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A만 정렬 가능 
# B를 왜 정렬하면 안되는거지?
# 가장 작은 수가 나오려면 가장 큰수에 가장 작은 수가 곱해져야 함
A.sort()
B.sort(reverse=True)

C=0
for i in range(N):
    C += A[i]*B[i]
print(C)
