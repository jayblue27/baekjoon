import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))    
houses.sort()

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
    cnt = 1

    for i in range(1, len(houses)):
        if houses[i] >= current + mid:
            cnt += 1
            current = houses[i]

    if cnt >= C:        
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans)
