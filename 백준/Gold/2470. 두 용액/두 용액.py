#백준 - 두 용액 - 골드 5

'''
산성 용액과 알칼리 용액 주어진다.
0에 가장 가까운 두 숫자 찾기

정렬하고 투포인터로 움직이며
절대값이 가장 작은 두 수 출력
'''
import sys
#입력
N = int(input())
arr = list(map(int, input().split()))

arr.sort() # 투포인터 사용을 위한 정렬
l,r = 0,N-1 # 포인터 설정

ans = sys.maxsize
ans_list = []

# 투포인터
while l < r:
    tmp_sum = arr[l]+arr[r]
    # 두용액합 0과 가장 가까운 용액 구하기
    if abs(tmp_sum) < ans:
        ans = abs(tmp_sum)
        arr_list = [arr[l], arr[r]]
    
    if tmp_sum <0:
        l += 1
    else:
        r -= 1

print(*arr_list)