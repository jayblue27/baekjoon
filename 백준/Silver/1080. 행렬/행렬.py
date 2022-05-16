# 행렬
'''
0과 1로 이루어진 행렬 A와 B
A를 B로 바꾸는데 필요한 연산횟수의 최솟값 구하기
* 연산 : 3x3크기의 부분행렬의 원소 뒤집기

- 입력
1. 행렬의 크기 N,M <=50
2. 행렬 A
3. 행렬 B

-출력 
최소횟수 , A를 B로 못만들 때 -1 출력

3 4
0000
0010
0000
1001
1011
1001
>> 2

3 3
111
111
111
000
000
000
>> 1
'''

#입력
N, M = map(int, input().split())
A = [ list(map(int, input())) for _ in range(N)]
B = [ list(map(int, input())) for _ in range(N)]

def reverse(i, j):
    '''
    3x3 부분행렬 뒤집기 함수
    i,j : 시작할 좌표
    '''
    for x in range(i, i+3):
        for y in range(j, j+3):
            #0이면 1로, 1이면 0으로 
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0

cnt = 0 
# 예외처리 행렬이 3x3 보다 작고, A랑 B랑 다를경우 변환 불가함
# 첫번째 요소가 다르면 바꿔줘야 함
if (N < 3 or M < 3) and A != B:
    cnt = -1
else:
    #모든 행렬 순환    
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]: #첫번째 원소의 값이 다르면               
                reverse(i, j) # 뒤집기 함수 실행
                cnt += 1 

    if A != B: # A와 B가 같은지 확인
        cnt = -1

print(cnt)