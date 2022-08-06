def solution(numbers):
    numbers = list(map(str, numbers)) 
    # print(numbers)
    #num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
    numbers.sort(key = lambda x : x*3, reverse = True) 
    # print(numbers)
    #모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.
    return str(int(''.join(numbers)))