S = input()

ans = []
for i in range(len(S)):
    for j in range(i,len(S)):
        tmp = S[i:j+1]
        ans.append(tmp)

print(len(set(ans)))