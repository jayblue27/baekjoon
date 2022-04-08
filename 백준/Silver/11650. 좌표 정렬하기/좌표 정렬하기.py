# 입력 - 좌표 수
N = int(input())

# 입력 - 좌표
XY = []
for i in range(N):
    x,y = map(int, input().split())
    XY.append([x,y])

# 각자 정렬하면 틀림
# 퀵 정렬 함수
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

#정렬
XY = quick_sort(XY)

#출력
for i in range(len(XY)):
    print(XY[i][0],end=' ')
    print(XY[i][1])