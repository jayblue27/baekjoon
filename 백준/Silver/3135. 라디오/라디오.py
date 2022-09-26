# 라디오 - 실버 5
'''
라디오 수집광

1번쨰 버튼 1MHz 증가
2번째 버튼 1MHz 감소
나머지 N개의 버튼 즐겨찾기 미리지정된 주파수 이동

A,B : A에서 B로 갈때 눌러야 하는 버튼의 최수값
N : 미리 지정된 주파수
hz_array : N개의 지정된 주파수

정렬 필요?

hz_array 순회 하면서 B - 현재 값 정하고

즐겨찾기 버튼으로 최대한 가까이 가고
나머지는 1씩 증가 혹은 감소(절대값으로)
즐겨찾기 버튼 누르는것도 버튼 +=1

즐겨찾기를 누르는경우(즐겨찾기 누르기(+1) + 즐겨찾기에서 b까지 가는 거리) 
vs 안누르는 경우(a에서 b바로 가는 경우)
'''

# a, b = 64, 120
# n = 1
# hz_array = [567]

import sys
input = sys.stdin.readline
del input

a,b = map(int, input().split())
n = int(input())
hz_array = []
for _ in range(n):
    hz_array.append(int(input()))

cnt = abs(b-a)

for i in range(len(hz_array)):
    hz_array[i] = abs(b - hz_array[i])
    
print(min(cnt, min(hz_array)+1))