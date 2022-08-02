S = [input() for _ in range(5)]
i = 0
max_len = max(map(lambda x:len(x), S))
while i < max_len:
    for j in range(5):
        if i+1 > len(S[j]):
            continue
        print(S[j][i], end='')
    i += 1
print()