# 마트료시카 합치기 - 실버5

'''
N개의 마트료시카 
남아있는 최소 마트료시카 구하기

큰수부터 작아지면서 

counter로 counting values중에 가장 작은 수 return시도
'''
from collections import Counter

n = int(input())
dolls = list(map(int,input().split()))

cnt = Counter(dolls)
print(max(cnt.values()))