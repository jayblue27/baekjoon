# 백준 - 개수 세기 - 브론즈 5
from collections import Counter
N = int(input())
arr = Counter(map(int,input().split()))
v = int(input())
print(arr[v])