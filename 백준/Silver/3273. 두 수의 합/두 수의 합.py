# 백준 - 두 수의 합
# target값이 되는 수들의 합 

# 입력1. 수열의 크기
n = int(input())
# 입력2. 수열
arr = list(map(int,input().split()))
arr.sort()
# 입력3. target 값
x = int(input())

# 포인터 설정
left, right = 0, n-1
# 조건을 만족하는 경우 카운팅
cnt = 0 

# 좌우 끝에서 시작하는 두 포인터를 쓰려면 정렬이 되어있어야 한다
while left < right:
    sum_num = arr[left] + arr[right]
    if sum_num == x:
        cnt += 1
        left += 1
    
    elif sum_num < x:
        left += 1
    
    else:
        right -=1

print(cnt)