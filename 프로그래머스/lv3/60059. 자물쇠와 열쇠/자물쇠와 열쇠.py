'''
열쇠 회전 가능
회전(4) * 이동(상하좌우 끝-1 까지)

4가지경우 - 0도, 90도, 180도, 270도

돌기끼리 만나면 안됨 -> 모든 값이 1이면 true 

'''

def match(arr, key, rot, r, c):
    n = len(key) # 열쇠의 크기
    for i in range(n):
        for j in range(n):
            # 이부분 제대로 이해 못함 -> 직접 그려보면서 이해
            if rot == 0:
                arr[r+i][c+j] += key[i][j]
            elif rot == 1:
                arr[r+i][c+j] += key[n-1 -j][i]
            elif rot == 2:
                arr[r+i][c+j] += key[n-1 -i][n-1 -j]
            else:
                arr[r+i][c+j] += key[j][n-1 -i]

def check(arr, offset, n):
    for i in range(n):
        for j in range(n):
            if arr[offset+i][offset+j] != 1:
                return False
    return True
            

def solution(key, lock):
    offset = len(key) -1
    
    # 모든 경우의 수 탐색 (offset 준 행,열 좌표 값 * 회전)
    # 행 
    for r in range(offset + len(lock)):
        for c in range(offset + len(lock)):
            for rot in range(4):
                arr = [[0 for _ in range(58)] for _ in range(58)]
                for i in range(len(lock)):
                    for j in range(len(lock)):
                        arr[offset+i][offset+j] = lock[i][j]
                        
                match(arr, key, rot, r, c)
                if check(arr, offset, len(lock)):
                    return True
    return False
                
                        