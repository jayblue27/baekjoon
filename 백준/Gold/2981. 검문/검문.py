from math import gcd
from math import sqrt


N = int(input())
arr = list(int(input()) for _ in range(N))
arr.sort()

gap = []
ans = []

for i in range(1, N):
    gap.append(arr[i] - arr[i - 1])

prev = gap[0]
for i in range(1, len(gap)):
    prev = gcd(prev, gap[i])

for i in range(2, int(sqrt(prev)) + 1): #제곱근까지만 탐색
    if prev % i == 0:
        ans.append(i)
        ans.append(prev//i)
ans.append(prev)

ans = list(set(ans)) #중복이 있을수 있으니 제거
ans.sort() # 오름차순 정렬

print(*ans)