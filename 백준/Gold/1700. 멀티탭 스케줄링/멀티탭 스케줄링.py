import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
m = [*map(int, input().split())]
multitab = set()
counter = Counter(m)
answer = 0
for i, x in enumerate(m):
    counter[x] -= 1
    if x in multitab:
        continue
    if x not in multitab and len(multitab) >= n:  
        for a in multitab:  
            if counter[a] == 0:
                multitab.remove(a)
                answer += 1
                break
        else:
            temp_set = set()
            for j in range(i, k):
                if m[j] in multitab:
                    temp_set.add(m[j])
                if len(temp_set) == n:
                    multitab.remove(m[j])
                    break
            answer += 1
    multitab.add(x)
print(answer)