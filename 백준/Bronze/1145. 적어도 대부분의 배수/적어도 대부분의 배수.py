# 5개의 자연수 -> 최소 공배수 찾기 
# n을 min(arr) 부터 1씩 늘려가며, 3개이상의 숫자로 나눠지는지 검사하고
# if 3개 이상이경우 n return else: n += 1

arr = list(map(int, input().split()))
n = min(arr)

while True:
    cnt = 0
    for i in range(len(arr)):
        if n % arr[i] == 0:
            cnt += 1
    
    if cnt >= 3:
        print(n)
        break
    else:
        n += 1
