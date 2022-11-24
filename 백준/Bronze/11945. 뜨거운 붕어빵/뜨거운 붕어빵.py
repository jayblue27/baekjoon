# 백준 - 뜨거운 붕어빵
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))

for a in arr:
    print(''.join(a[::-1]))