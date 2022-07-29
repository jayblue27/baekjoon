# 백준 - 수들의 합2 (두 포인터 )

import sys
input = sys.stdin.readline

# 입력 
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 포인터 설정
left, right = 0, 1
cnt = 0   # 카운트

# right는 길이를 넘으면 안되고 left는 right를 넘으면 안된다
while right<=N and left<=right:
    num_sliced = nums[left:right]
    sum_num_sliced = sum(num_sliced)

    # 계산한 값이 M(target)과 같으면 cnt 올리고 right 한칸 오른쪽
    if sum_num_sliced == M:
        cnt += 1
        right += 1

    # M보다 작을 경우에는 right를 한칸 늘려서 값을 더 한다.
    elif sum_num_sliced < M:
        right += 1

    # 값이 M보다 클 경우에는 left를 올린다.
    else:
        left += 1

print(cnt)