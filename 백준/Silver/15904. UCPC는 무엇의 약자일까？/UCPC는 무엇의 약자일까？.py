#백준 - UCPC는 무엇의 약자일까
from collections import deque

#입력
text = input()
filter = deque(['U','C','P','C'])

tmp = ''
for i in text:
    # 덱의 첫번째 요소와 일치할 때 
    if i == filter[0]:
        # 덱의 요소를 팝 레프트 해서 tmp문자열에 저장
        tmp+=filter.popleft()

    #tmp 값이 UCPC면 출력 반복문 종료
    if 'UCPC' == tmp:
        print('I love UCPC')
        break
# 그외 케이스 출력 
else:
    print('I hate UCPC')