#백준 공유기 설치 - 이분 탐색

# N, C = 5, 3
# houses = [1, 2, 8, 4, 9]

# 하고 안하고 차이 많이 나니까 웬만하면 하자
import sys
input = sys.stdin.readline

# 입력
# N개의 집(2이상), C개의 공유기
N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))    
houses.sort() #정렬


start = 1
# start = houses[0]
end = houses[-1] - houses[0]
# end = houses[-1]
ans = 0
# 이부분 이해
# start가 end보다 같거나 커지기 전까지

while start <= end:
    mid = (start + end) //2 
    current = houses[0]
    cnt = 1 # 분기점 사이의 집개수를 세는 변수

    # 현재위치와 집의 거리가 mid 이상이면
    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            cnt += 1
            current = houses[i]
    # count값이 C 이상이면
    if cnt >= C:        
        start = mid + 1
        ans = mid
    # C 미만이면
    else:
        end = mid - 1

print(ans)