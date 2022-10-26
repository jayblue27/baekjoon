n = int(input())
v = list(map(int, input().split(' ')))

max_v = max(v)
print(sum(v) - max_v)