#백준 - 숫자 카드 2

# N과 N개의 숫자 카드가 있음, 
# M과 M개의 숫자 카드가 주어졌을 때 
# M의 원소에 해당하는 숫자카드가 N 리스트에 몇개 있는지 리스트 형태로 반환

from sys import stdin
from collections import Counter

from sys import stdin
from collections import Counter
_ = stdin.readline()
N = stdin.readline().split()
_ = stdin.readline()
M = stdin.readline().split()

#N의 원소가 몇개 있는지 dict 형태로 반환
C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))