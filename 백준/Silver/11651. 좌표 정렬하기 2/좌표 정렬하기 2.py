N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int,input().split())))

lst.sort()
lst.sort(key=lambda x:x[1])

for i, j in lst:
    print(i,j)