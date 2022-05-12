# 백준 앵그리창영
# 대각선으로도 들어가진다.
# 꽉 채우는 문제가 아니라. 

import sys
input = sys.stdin.readline
#반복수, 폭, 높이
n, w, h = map(int, input().split())
#case 반복
for i in range(n):
    # 성냥길이 입력
    b = int(input().strip())
    # 대각선 구하기 
    # 피타고라스의 정리 a^2 + b^2 = c^2
    l = (w ** 2 + h ** 2) ** 0.5
        
    if b <= l:
        print("DA")
    else:
        print("NE")
    