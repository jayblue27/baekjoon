from itertools import combinations
import math

'''
itertools로는 계산이 불가함 ram사용량 초과
조합공식 찾아서
nPr = n!/(n−r)!​​
nCr = nPr / r! 
''' 
n,m = map(int,input().split())
print(int( math.factorial(n) // math.factorial(n-m) // math.factorial(m) ))
