n = int(input())
d = [0] * (n+1)
def zero_one(n):
    if n < 3:
        return n
    d[1] = 1
    d[2] = 2
    for i in range(3,n+1):
        d[i] = (d[i-2] + d[i-1])%15746
    return d[n]

print(zero_one(n))