s = input()
arr = ['a','e','i','o','u']

cnt = 0
for c in s:
    if c in arr:
        cnt += 1
print(cnt)