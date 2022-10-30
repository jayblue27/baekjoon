'''
노란색, 갈색 개수는 기억
전체 카펫트 크기 유추 

가로가 세로보다 길거나 같다.

1. yellow 크기 정렬
2. brown + yellow 정렬 만들기 

3. 1번좌표 x+2, y+2 == 2번좌표 일경우 return

'''
def making_code(num):
    arr = []
    for i in range(1, num+1):
        if num%i == 0 and i <= num//i:
            arr.append([i,num//i])
    return arr
    
def solution(brown, yellow):
    yellow_arr = making_code(yellow)
    y_and_b_arr = making_code(brown+yellow)
    
    answer = []
    for yx,yy in yellow_arr:
        for ybx, yby in y_and_b_arr:
            if yx+2 == ybx and yy+2 == yby:
                return [yby,ybx]
                