def solution(n, towers):
    cnt = 1
    for i, t in enumerate(towers):
        if i == 0:
            tmp = towers[0]
        else:
            if tmp <= t:
                cnt += 1
            tmp = t
    print(cnt)

if __name__ == '__main__':
    n = int(input())
    towers = list(map(int,input().split()))
    solution(n, towers)