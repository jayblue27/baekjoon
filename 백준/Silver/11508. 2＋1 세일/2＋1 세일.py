from sys import stdin

N = int(stdin.readline())
product = []
for i in range(N):
    product.append(int(stdin.readline()))
product.sort(reverse=True)

total = 0
for i, p in enumerate(product):
    if i%3!=2 : total+=p
print(total)