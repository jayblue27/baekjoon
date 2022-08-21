entire = set(range(1,31))
submit = []
ans = {}

for _ in range(28):
    submit.append(int(input()))

ans = entire - set(submit)

print(min(ans))
print(max(ans))