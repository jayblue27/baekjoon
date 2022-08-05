word = input()
ans = ''

for w in word:
    if w.isupper():
        ans += w.lower()
    else:
        ans += w.upper()

print(ans)