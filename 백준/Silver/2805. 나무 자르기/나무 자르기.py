#백준 - 나무자르기 - 이분탐색

#M 미터의 나무 
#높이 H 지정 H보다 큰 나무는 잘리고 아니면 안잘린다.
# M미터의 나무를 가져가기위해 설정할 수 있는 H의 최대값

#입력
#1. 나무수 N개, 가져가고싶은 길이 M
#2. N개의 나무 높이 
import sys
input = sys.stdin.readline
N, M = map(int,input().split()) 
trees = list(map(int, input().split()))

#시작점, 끝점 설정
start, end = 0, max(trees)

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0 # 잘린 나무 합
    for i in trees:
        if i > mid: 
            tree += (i - mid)

    if tree >= M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)