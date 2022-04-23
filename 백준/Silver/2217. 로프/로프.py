N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))


arr.sort(reverse=True)

new_arr = [0] * N
for i in range(N):
    new_arr[i] = arr[i] * (i+1)

print(max(new_arr))