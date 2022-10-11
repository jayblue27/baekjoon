#연산자 끼워넣기 - 실버1
'''
N개의 수로 이루어진 수열 A 
수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자

만들 수 있는 최대, 최소 값 구하라 

음수를 나눌때 C++14 기준으로 하라고 하는데
// 연산자로 나누면 -1//3 -> -1 나오고
int() + / 연산자로 풀이하면 0이 나온다
-> 머리 아프니까 일단 넘어가자

이 문제에서는 int() + / 로 사용해야 예시 3번의 결과를 얻을 수 있다.
'''
import sys
input = sys.stdin.readline

#입력
# n : 수의 개수
n = int(input())
# A : 수열
A = list(map(int, input().split()))
# 연산자 개수 + - * / 순 (0 0 1 0) -> 곱하기만 한개
op_lst = ['+','-','*','/']
op_lst_count = list(map(int,input().split()))

# 입력받은 연산자 문자열로 더하기(순열 구하기 용도)
operators = ''
for i in range(4):
    operators += op_lst[i] * op_lst_count[i]

# 연산자의 모든 순열 구한다.
from itertools import permutations
op_permutations = list(permutations(operators, len(operators)))

# 문자열을 연산자로 돌리기 위한 라이브러리 및 딕셔너리
import operator
op_dict = {'+':operator.add, '-':operator.sub,
           '*':operator.mul, '/':operator.truediv}

# 최대, 최소값 변수 선언
ans_max = -10e9
ans_min = 10e9

# 수열의 첫 숫자를 변수에 넣고, 모둔 경우의 수 연산
for op_tup in op_permutations:
    tmp = A[0]
    for i in range(len(op_tup)):
        tmp = int(op_dict[op_tup[i]](tmp, A[i+1] ))
    
    ans_max = max(ans_max, tmp)
    ans_min = min(ans_min, tmp)

print(ans_max)
print(ans_min)