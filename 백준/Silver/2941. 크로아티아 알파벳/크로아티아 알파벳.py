#정규표현식 라이브러리
import re 
# 리스트 생성
abc = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 문자열 입력
s = input()

# 숫자 돌리기
for i in abc:
    if re.search(i, s):
        s = s.replace(i, 'x')

print(len(s))