f = [0, 1]
for i in range(2, 50):
    f.append(f[i-2] + f[i-1])

T = int(input())

for j in range(T):
    n = int(input())

    array = []

    while (n):
        for k in range(50):
            if (f[k] <= n):
                t = f[k]

        n = n - t
        array.append(t)
        array.sort()

    for l in array:
        print(l, end=' ')