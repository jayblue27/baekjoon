# 도서관 - 골드 5
'''
도서관 책을 다시 가져다 놓아야 한다. 
현재 위치 0(세준, 책)
책들의 원래 위치 주어지고, 모두 가져다 놓을 때
거리산정

한 번에 최대 M권의 책을 들 수 있다. 
원래 자리로 돌아올 필요는 없다. 
책의 위치가 0인 경우는 없다. 

1. 절대값이 가장 큰수를 왕복없이 다녀오는게 제일 이득이다. 
  - 0으로 꼭 안돌아와도 괜찮지만, 한 번에 옮길 수 있는 책의 수가 정해져있어서 
  - m권의 책을 가져다두고 남아있으면 또 가지러 와야함
2. 음과 양은 따로 간다 (왼쪽 갔다 오른쪽 갔다 손해)
'''
# n, m = 7, 2
# arr = [*map(int, '-37 2 -6 -39 -29 11 -28'.split())]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [*map(int, input().split())]

pos = []
neg = []
max_dist = 0 # 제일 멀리 있는 책의 위치

for i in arr:
    # 양수와 음수를 나눈다.
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)

    # 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요 없기때문에
    # 마지막 책은 제일 멀리 있는 책으로 정한다.
    if abs(i) > abs(max_dist):
        max_dist = i

# 양수는 내림차순으로 음수는 오름차순으로 정렬한다.
pos.sort(reverse= True)
neg.sort()

# 결과 담을 변수 선언
dist = 0

# m권을 들고 양수 방향에 책을 모두 제자리에 놔둔다.
for j in range(0, len(pos), m):
    # 제일 멀리 있는 책은 무시한다.
    if pos[j] != max_dist:
        dist += pos[j]

# m권을 들고 음수 방향에 책을 모두 제자리에 놔둔다.
for k in range(0, len(neg), m):
    # 제일 멀리 있는 책은 무시한다.
    if neg[k] != max_dist:
        # 거리를 계산하기 위해 절대값으로 바꿔 더한다.
        dist += abs(neg[k])
        
# 거리는 책의 제자리 위치와 현재 책의 위치를 왕복하여 계산한다.
dist *= 2
# 제일 멀리 있는 책 왕복 없이 더한다. 
dist += abs(max_dist)

print(dist)