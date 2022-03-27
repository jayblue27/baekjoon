#세자리 수 2개 입력 받음
#숫자 자리를 바꿔서 2수를 비교한 뒤 큰 수를 출력

# 숫자 순서 바꿔주는 함수
def reverse_number(num):
    tmp = ''
    return int(tmp+num[2]+num[1]+num[0])

#입력 
A, B = input().split()

#숫자 바꾸기
A = reverse_number(A)
B = reverse_number(B)

#큰수 판별기
if A > B:
    print(A)
elif A < B:
    print(B)