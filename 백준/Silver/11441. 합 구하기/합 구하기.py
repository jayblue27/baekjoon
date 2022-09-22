#백준 - 합구하기 - 구간합으로
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

sum_value = 0
prefix_sum = [0]
for i in arr:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(int(input())):
    l, r = map(int,input().split())
    print(prefix_sum[r]-prefix_sum[l-1])
