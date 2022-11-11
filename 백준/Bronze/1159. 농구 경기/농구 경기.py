from collections import defaultdict
n = int(input())

dic = defaultdict(int)
for _ in range(n):
    t = input()
    dic[t[0]] += 1
    
answer = []
for k,v in dic.items():
    if v >= 5:
        answer.append(k)

if answer:
    print(''.join(sorted(answer)))
else:
    print('PREDAJA')