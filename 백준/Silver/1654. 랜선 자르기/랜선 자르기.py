#백준 - 랜선자르기 - 이분탐색

#문제 
# N개의 랜선 필요함
# K개의 랜선을 잘라서 만들어야 함

# 입력
# K : 가지고 있던 랜선 개수, N 필요한 랜선갯수


# K, N = 4, 11
# cables_K = [802, 743, 457, 539]

K, N = map(int, input().split())
cables_K = []
for _ in range(K):
    cables_K.append(int(input()))

start, end = 1, max(cables_K)

while start <= end:   
    mid = (start+end)//2
    tmp = 0 # 몫 담을 변수

    #몫을 계산하고
    for i in cables_K:
        tmp += i//mid
        if tmp >= N:
          break  
    
    #tmp 갯수가 N보다 크거나 같으면 숫자를 키워야지 
    if tmp >= N:
        start = mid + 1
    #tmp 갯수가 N보다 작으면 숫자를 mid보다 낮춰야 하고
    else:
        end = mid - 1

print(end) 