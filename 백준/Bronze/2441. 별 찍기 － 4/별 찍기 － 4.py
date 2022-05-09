n = int(input())
a = list(range(n))
b = list(range(n,0,-1))
for i, j  in zip(a,b):
    print((' '*i) +('*'*j))