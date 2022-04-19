def divisor(n =int(input())):
    '''
    입력 예를 보니까 
    배열내 최대값 x2 가 결과인 줄 알았는데 틀림

    반례에 대한 이해를 못함
    '''
    nums = list(map(int, input().split()) )
    ans = max(nums) * min(nums)
    return ans

print(divisor())