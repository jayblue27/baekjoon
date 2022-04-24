#백준 - 30 
# 30의 배수는 자리수를 다 더해서 3의 배수가되고, 맨 끝자리가 0이면 된다. 
# 양수 N
N = input()
N = sorted(N, reverse=True)
sum = 0

# 0이 없으면 -1
if '0' not in N:
    print(-1)
else:
    #자릿수 더하기
    for i in N:
        sum += int(i)
    # 3으로 못나누면 -1
    if sum%3 != 0:
        print(-1)
    # 그 외 출력
    else:
        print(''.join(N))