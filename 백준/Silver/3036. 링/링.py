#백준 - 링 - 실버4
'''
N개의 링 3<= N <= 100
'''
def GCD(a,b):
    remainder = a%b

    if remainder == 0:
        return b
    else:
        return GCD(b,remainder)

N = int(input())
nums = list(map(int,input().split()))

for i in range(1, len(nums)):
    answer = ''
    num = GCD(max(nums[0], nums[i]), min(nums[0],nums[i]))
    answer += str(nums[0]//num) + '/' + str(nums[i]//num)
    print(answer)