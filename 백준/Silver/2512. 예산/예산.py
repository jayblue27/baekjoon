#백준 - 예산

#입력 
#N: 지방의 수 
#N개의 예산 요청
#총 예산 M

import sys
input = sys.stdin.readline

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())

start = 1
end = max(n_lst)
while start <= end:
    budget = 0
    mid = (start+end) //2
    for i in n_lst:
        if i < mid:
            budget += i
        else:
            budget += mid

    if budget <= M:
        start = mid+1
    else:
        end = mid-1

print(end)
