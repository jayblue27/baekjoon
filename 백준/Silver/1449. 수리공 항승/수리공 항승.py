#입력
N, L = map(int, input().split())
locs = list(map(int,input().split()))

#정렬
locs.sort()
#테이프 수
cnt = 0

tmp = 0
for loc in locs:
    # 
    if tmp < loc:
        cnt += 1
        tmp = loc + L - 1
#출력
print(cnt)