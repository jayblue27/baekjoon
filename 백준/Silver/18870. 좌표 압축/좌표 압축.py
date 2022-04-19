N = int(input())
arr = list(map(int, input().split(' ')))


# dict 만들기
# list(set(sorted(arr)))# -> 이렇게 하니까 정렬이 풀린다.
arr_tmp = list(set(arr))
arr_tmp.sort()

ans_list = {}
for i in range(len(arr_tmp)):
    ans_list[arr_tmp[i]] = i

# 출력
for i in arr:
    print(ans_list[i], end=' ')