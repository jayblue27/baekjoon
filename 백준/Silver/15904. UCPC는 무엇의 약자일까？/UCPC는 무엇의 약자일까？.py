#백준 - UCPC는 무엇의 약자일까
from collections import deque

text = input()
filter = deque(['U','C','P','C'])

tmp = ''
for i in text:
    if i.isupper() and i in filter[0]:
        tmp+=filter.popleft()

    if 'UCPC' == tmp:
        print('I love UCPC')
        break

else:
    print('I hate UCPC')