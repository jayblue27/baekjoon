k = int(input())
for i in range(1,k+1):
    tmp = list(map(int, input().split()))
    n = tmp[0]
    arr = tmp[1:]
    arr.sort()

    gap = 0
    for j in range(1, len(arr)):
        gap = max(gap, abs(arr[j]- arr[j-1]))

    print(f'Class {i}')
    print(f'Max {arr[-1]}, Min {arr[0]}, Largest gap {gap}')   