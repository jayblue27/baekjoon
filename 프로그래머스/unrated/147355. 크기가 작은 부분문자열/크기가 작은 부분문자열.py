from bisect import bisect_left, bisect_right
def solution(t, p):
    n = len(p)
    arr = []
    
    # 부분 숫자 다 만들고
    for i in range(len(t)-n+1):
        arr.append(int(t[i:i+n]))
        
    arr.sort()
    return bisect_right(arr, int(p))
    
    # return arr
        
    # 오름차순 정렬 
    
    # answer = 0
    # return answer