import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

dic = dict()

for i in arr:
    if i not in dic:
        dic[i] = 0

    dic[i] += 1


dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for a, b in dic:
    for j in range(b):
        print(str(a)+" ",end="")