# 배열 합치기
'''
정렬된 두배열 A,B
합친 다음 출력
'''
from collections import deque

# 두 배열 A,B의 크기 N,M
N,M = map(int,input().split())
# A의 내용
A = list(map(int, input().split()))
# B의 내용
B = list(map(int, input().split()))

# 풀이
i,j = 0, 0

result = []
while len(result)<(N+M) :
    # 예외 처리 
    # 한쪽이 끝에 도달 했을 때, 반대 배열의 값 append 및 인덱스 증가
    if i == N:
        result.append(B[j])
        j+=1
    elif j == M:
        result.append(A[i])
        i+=1
    # 그 외
    else:
        # 비교해서 작은 쪽 먼저 append 후 index 1씩 증가
        if A[i] < B[j]:
            result.append(A[i])
            i+=1
        else:
            result.append(B[j])
            j+=1

#출력
print(*result)