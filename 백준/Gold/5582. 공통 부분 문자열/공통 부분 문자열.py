a = '0' + input()
b = '0' + input()
a_len = len(a)
b_len = len(b)
lcs = [[0] * b_len for _ in range(a_len)]
res = 0

for i in range(1, a_len):
    for j in range(1, b_len):
        if a[i] == b[j]:
            lcs[i][j] = lcs[i-1][j-1] + 1
            res = max(res, lcs[i][j])

print(res)