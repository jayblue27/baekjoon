K, N, M = map(int, input().split())

price = K*N

if M < price:
    print(price-M)
else:
    print(0)