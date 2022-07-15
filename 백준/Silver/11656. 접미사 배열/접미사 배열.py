# 접미사 배열 - 실버4

S = input()

res = []
for i in range(len(S)):
    res.append(S[i:])

for w in sorted(res, key=lambda x:x):
    print(w)