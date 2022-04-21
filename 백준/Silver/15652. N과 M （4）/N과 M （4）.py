# itertools 공부 더 해보기
from itertools import combinations_with_replacement as cr
n,m = map(int,input().split())
lst = [i+1 for i in range(n)]
result = list(cr(lst,m))
for item in result:
    print(*item)