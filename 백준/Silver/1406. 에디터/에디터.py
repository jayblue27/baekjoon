#백준 - 에디터
'''
영어 소문자만을 기록할 수 있는 편집기
최대 600,000글자 까지 입력 가능하다. 

처음의 커서 위치는 맨 뒤에 위치
'''

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
            
    elif cmd[0] == 'D':
        if st2:
        	st1.append(st2.pop())

    elif cmd[0] == 'B':
    	if st1:
        	st1.pop()
            
    else:
    	st1.append(cmd[1])
        
st1.extend(reversed(st2))
print(''.join(st1))