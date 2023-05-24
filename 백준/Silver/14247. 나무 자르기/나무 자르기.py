from typing import List
import sys

# n개의 나무
# 하루에 한나무씩 n일 산에 오른다. 
# 나무마다 자라는길이가 다름
# 어느 나무를 먼저 자르는지에 따라 총 구할 수 있는 나무의 양이 다름 
# 영선이가 얻을 수 있는 최대 나무의 양
# 자른 이후에도 0부터 다시 자고(한 나무를 여러번 자를 수 있다.)

#input
# n : 나무의 개수
# H : 최초 나무의 길이
# A : 나무들이 자라는 길이

# 처음 자를게 많을수록 -> 먼저
# 속도가 느릴수록 나중에

def solution(n : int, H : List[int], A : List[int]) -> int: 
    # 두 리스트를 합치고
    arr = list(zip(H, A))
    arr.sort(key=lambda x: (x[1], -x[0]))

    ans = 0
    for i in range(n):
        ans += arr[i][0] + (arr[i][1] * i)
    
    return ans
    # H기준 내림차순
    # A기준 오름차순 
    # for 돌면서 H + A*(i+1) 값을 더한다.  

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    H = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # n = 5
    # H = [1,3,2,4,6]
    # A = [2,7,3,4,1]

    print(solution(n, H, A))
