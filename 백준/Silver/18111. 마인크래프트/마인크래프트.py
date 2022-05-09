# 백준 - 마인크래프트 - 부르트포스
# import sys
# input = sys.stdin.readline

#입력
N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.extend(map(int, input().split()))

# N,M,B = 3, 4, 0  # 3줄, 4열, 가진 블록 수 0개 
# blocks = [64, 64, 64, 64,
#           64, 64, 64, 64,
#           64, 64, 64, 63]

# 층수별로 블록이 몇개 있는지 확인
block_count = [0 for _ in range(257)]

for i in blocks:
    block_count[i] += 1

#시간  #최대높이
소요시간, 높이 = float('inf'), 0  # 소요시간이 10000000보다 크게 나오는 답이 있어서 틀렸다고 나온다는데

for h in range(257): 
    p = 0
    m = 0
    for b in range(257):
        if h > b:
            p += (h - b) * block_count[b]
        else:
            m += (b - h) * block_count[b]
    inven = B + m - p
    if inven < 0:
        continue
    t = m * 2 + p
    if t <= 소요시간:
        소요시간 = t
        높이 = h

print(소요시간, 높이)