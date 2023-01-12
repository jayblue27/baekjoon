import sys
input=sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
arr_reverse = arr[::-1]

ans = sys.maxsize
for i in range(len(arr)//2):
    ans = min(ans, arr[i]+arr_reverse[i])

print(ans)
