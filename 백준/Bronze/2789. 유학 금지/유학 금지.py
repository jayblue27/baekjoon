arr = list('CAMBRIDGE')
n = input()
ans=''

for c in n:
    if c in arr:
        continue
    ans+=c
print(ans)