# 돌게임 2 - 실버5
'''
N개의 돌
한번에 1개 혹은 3개를 가져갈 수 있다.

n이 홀수일 때 
창영이가 이기고
n이 짝수면 SK가 이긴다.
'''
n =int(input())
if n % 2 == 0: print('SK')
else: print('CY')