# 백준 - 문자열 - 브론즈5
'''
주어진 문자열의 처음과 끝 출력
'''
N = int(input())

for _ in range(N):
    tmp = input()
    print(tmp[0]+tmp[-1])   