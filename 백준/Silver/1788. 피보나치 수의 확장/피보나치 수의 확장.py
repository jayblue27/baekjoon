from sys import stdin

fibo = [0 for _ in range(1500000)]
n = int(stdin.readline())
fibo[0:1] = [0, 1]

if n < 0:
    for i in range(-1, n - 1, -1):
        data = fibo[i+2] - fibo[i+1]
        if data < 0:
            fibo[i] = (abs(data) % 1000000000) * -1
        else:
            fibo[i] = data % 1000000000
    if fibo[n] < 0:
        print(-1)
        print(fibo[n] * -1)
    else:
        print(1)
        print(fibo[n])


elif n > 0:
    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1000000000

    print(1)
    print(fibo[n])

else:
    print(0)
    print(0)