s = input()
new_s = ''

for c in s:
    if c.isalnum():
        new_s += c.lower()

if new_s == new_s[::-1]:
    print(1)
else:
    print(0)
       