def F(num):
    arr = [j for j in range(num+1)]
    if num < 2:
        return num

    for i in range(2, num+1):         # 반복
        arr[i] = arr[i-1] + arr[i-2]

    return arr[num]

N = int(input())
for _ in range(N):
    M = int(input())
    if M == 0:
        print(1, 0)
    elif M == 1:
        print(0, 1)
    else:
        print(F(M-1), F(M))