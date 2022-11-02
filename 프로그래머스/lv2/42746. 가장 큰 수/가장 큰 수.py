'''
가장 큰 수

정렬을 제대로 하는게 핵심
문자로 바꿔서 내림차순 정렬하면 앞자리 기준으로 정렬하는데
테스트 케이스 2번의 경우 34 30 3으로 나온다.
34랑 30 사이에 어떻게 3을 끼워넣지
문자열을 2번 반복해서 34->3434 3-> 33 30 -> 3030

# 문자열로 미리 바꾸니까 0000의 경우 0000으로 나온다. 0으로 만들어줘야 하네
join한 값을 int로 
'''

def solution(numbers):
    #1. list 원소 문자열로 변경
    numbers = list(map(str, numbers))
    #2. 문자열의 2배 기준으로 내림차순 정렬 (1000이하의 숫자 4자리 까지 있기 때문에 곱하기 4)
    numbers.sort(key=lambda x:4*x, reverse=True)
    #3. 출력
    return str(int(''.join(numbers)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     numbers = list(map(str, numbers)) 
    
#     #num의 인수값이 1000 이하이므로 3자리수로 맞춘 뒤, 비교하겠다는 뜻.
#     numbers.sort(key = lambda x : x*3, reverse = True) 
#     # print(numbers)
#     #모든 값이 0일 때(즉, ‘000’을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다.
#     return str(int(''.join(numbers)))