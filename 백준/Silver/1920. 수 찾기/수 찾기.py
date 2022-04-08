#입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이진 탐색을 하려면 오름차순 정렬이 되어 있어야 함
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

# arr_a : data, arr_b : target
def binary_search(arr_a, arr_b):
    # breakpoint()
    #arr_a 오름차순 정렬
    arr_a = quick_sort(arr_a)
    
    for i in range(len(arr_b)):
        # start, end 초기화
        start = 0
        end = len(arr_a) - 1 # 왜 마이너스 1?

        while start <= end:
            mid = (start + end) // 2
            # 중간값이랑 같으면
            if arr_a[mid] == arr_b[i]:
                print(1)
                break
            # 중간값보다 크면
            elif arr_a[mid] < arr_b[i]:
                start = mid + 1
            else:
                end = mid -1
        else:
            print(0)

binary_search(A,B)