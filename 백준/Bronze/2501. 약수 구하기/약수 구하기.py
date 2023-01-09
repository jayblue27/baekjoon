n, k = map(int, input().split())
j = 0
for i in range(1,int(n+1**(1/2))):
    if n%i == 0:
        j+=1
    if k == j:
        print(i)
        break
else:
    print(0)