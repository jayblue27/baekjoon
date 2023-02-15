import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))
summ = maxx = sum(arr[:k])
for i in range(k,n):
    summ = summ + arr[i] - arr[i-k]
    maxx = max(maxx, summ)
print(maxx)