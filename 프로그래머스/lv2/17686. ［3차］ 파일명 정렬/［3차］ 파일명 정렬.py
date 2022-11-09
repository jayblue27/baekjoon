'''
파일순 정렬
정렬시 ver-10.zip 의 숫자가 1부터 시작하기 때문에, ver-9.zip보다 앞에 정렬된다. 
숫자순으로 정렬하고 싶은데 

파일명은 아래 문자로 이뤄져있다. 
- 알파벳(대소문자)
- 숫자
- 공백
- 마침표
- 빼기 부호

!! HEAD, NUMBER, TAIL 로 구분 정렬
1. HEAD 기준 사전순 정렬 (대소문자 구분 x)
2. HEAD 같은 경우 number의 숫자순
3. HEAD, 숫자도 같을 경우 원래 입력순서 유지 ( MUZI01 muzi1 그대로) -> 숫자는 int로 바꿔서 비교


- head기준 사전순 정렬 먼저
- head랑 숫자랑 tail 어떻게 분리? 
    -> isdigit 써서 숫자 발라내고 
    -> 숫자 기준으로 split 하면 head와 tail 구할 수 있겠다. 
'''

# 런타임 에러 3,4,5,12,13,14,15,19,20 
# tail부분에 숫자가 다시 나타날 수 있다함

# 정규표현식 활용 숫자 추출 -> head, tail 구분
# 런타임 에러 13, 20 

# 같은 숫자가 반복되면 split 할때 ... 에러 발생
# 'abc123defg123.jpg' -> 123 기준으로 split하면 하 ...



import re

def solution(files):
    new_files = []
    for file in files:
        
        digits = re.search(r'[0-9]+',file)
        digit = digits[0]
        
        head, tail = file.split(digit, maxsplit=1)
        new_files.append([head,digit,tail])
    
    new_files.sort(key=lambda x:int(x[1]))
    new_files.sort(key=lambda x:x[0].lower())
    
    answer = [''.join(arr) for arr in new_files]
    
    return answer
        
    