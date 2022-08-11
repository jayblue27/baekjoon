import sys
N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1
answerL = 0
answerR = 0
_min = sys.maxsize # 임의의 최대값 지정 99999 와 같이 큰 숫자 지정하는거 지양해야함 더 큰 숫자가 지정될 수 있기 때문에 언제든지
while left<right:
    _sum = arr[left]+arr[right]

    if abs(_sum) < _min:
        answerL = left
        answerR = right
        _min = abs(_sum)

    if _sum > 0:
        right -= 1
    elif _sum < 0:
        left += 1
    else:
        break
print(arr[answerL], arr[answerR])