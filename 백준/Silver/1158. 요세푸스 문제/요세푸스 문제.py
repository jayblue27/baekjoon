# 입력
N, K = map(int, input().split())
people = list(range(1,N+1))
arr = []
idx = 0
while people:
    idx = (idx+K-1) % len(people)
    arr.append(str(people.pop(idx)))
print('<'+ ', '.join(arr) +'>')