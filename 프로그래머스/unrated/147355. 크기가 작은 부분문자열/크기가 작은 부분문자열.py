from bisect import bisect_left, bisect_right
def solution(t, p):
    n = len(p)
    arr = []
    
    # 부분 숫자 다 만들고
    for i in range(len(t)-n+1):
        arr.append(int(t[i:i+n]))
    
    # 정렬 후 
    arr.sort()
    # 2분탐색 통해서 index 반환
    return bisect_right(arr, int(p))
    