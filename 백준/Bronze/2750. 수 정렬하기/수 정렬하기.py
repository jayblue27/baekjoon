N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()) )

# 외부
def selection_sort(lst):
    for i in range(len(lst)-1):
        cur = i
        low = cur        
        for j in range(cur+1, len(lst)):
            if lst[low] > lst[j]:
                low = j
        lst[low],lst[cur] = lst[cur],lst[low]

    return lst 

selection_sort(lst)

for i in range(N):
    print(lst[i])