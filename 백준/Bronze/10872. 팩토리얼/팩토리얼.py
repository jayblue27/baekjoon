def fact(N):  
    if N == 0:
        return 1
    else:
        return fact(N-1) * N

print( fact(int(input())) )