# 주몽 - 실버4
'''
투포인터 -> target 넘버 카운팅 문제

1. 오름차순 정렬
2. 투포인터 검색
    - 타겟넘버 도달시 cnt+1 l+=1, r-=1
    - l==r break
'''

# #샘플값
# n,m = 6, 9
# arr = [2,7,4,1,5,3]

import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
arr = list(map(int,input().split()))
cnt = 0 #갑옷 수

#1. 정렬
arr.sort()

#2. 투포인터 검색
l,r = 0, len(arr)-1

while l != r:
    tmp = arr[l] + arr[r]
    if tmp == target:
        cnt+=1
        l+=1

    elif tmp < target:
        l+=1
    else:
        r-=1

print(cnt)