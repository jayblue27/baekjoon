def fibo(n):
    # breakpoint()

    if n == 0:   # case 1
        return 0
    elif n == 1:  # case 2
        return 1
    else:         # 그외
        return fibo(n-2) + fibo(n-1)

print(fibo(int(input())))