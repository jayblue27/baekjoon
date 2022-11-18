import sys
input = sys.stdin.readline

arr = []
for _ in range(5):
    arr.append(int(input()))
    
ans_mean = sum(arr) // 5

arr.sort()
ans_median = arr[2]

print(ans_mean)
print(ans_median)