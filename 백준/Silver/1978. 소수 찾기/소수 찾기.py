# 백준 - 소수 찾기
# https://www.acmicpc.net/problem/1978

N = int(input())
numbers = list( map( int, input().split() ) )

# numbers = [1 , 10, 11, 24]

cnt = 0
tmp = set()
for num in numbers:    
    if num == 1:
        N -= 1

    for i in range(2, num):
        if num%i == 0:
            tmp.add(num)                               

print(N - len(tmp))