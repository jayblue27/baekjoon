'''
1. 아이디어
- 백트래킹 재귀함수 안에서, for 순환하며 숫자 선택(방문여부 확인)
- 재귀함수에서 M개를 선택할 경우 print(종료조건)

2. 시간복잡도
- N! 
- 중복 없는 경우 N이 10까지 가능하며
- 해당문제 조건이 N <= 8 이므로 풀이 가능하다.

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
res = []
v = [0] * (N+1)

def bt(num):
    if num == M:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):
        if v[i] == 0:
            v[i] = 1
            res.append(i)
            bt(num+1)
            v[i] = 0
            res.pop()

bt(0)

