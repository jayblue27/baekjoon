# 백준 - 유기농 배추
'''
유기농 배추 키우려고 배추흰지렁이 구입
어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 민접한 다른 배추로 이동할 수 있음
*인접(상하좌우)
최소의 배추흰지렁이 마리 수 
DFS 이용 풀이
'''
# 재귀 limit 설정 
import sys 
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y): 
    # 상하좌우 확인을 위해 dx, dy 생성 
    dx = [0,0,-1,1] 
    dy = [1,-1,0,0] 
    
    # 네 방향 탐색 
    for i in range(4): 
        nx = x + dx[i] 
        ny = y + dy[i] 
        if (0 <= nx < X) and (0 <= ny < Y): # nx:ny ↔ X:Y10
         
            if matrix[ny][nx] == 1: 
                matrix[ny][nx] = -1 # 배추가 인접할 때 체커 
                dfs(nx, ny)

#입력 
# 테스트 케이스 
T = int(input().strip())

#배추밭 만들기 
for _ in range(T):    
    X, Y, cabbages = map(int, input().split())
    
    # 터 잡기
    matrix = [[0 for _ in range(X)]for _ in range(Y)] 
    
    # 배추 심기
    for _ in range(cabbages):
        x,y = map(int,input().split())
        matrix[y][x] = 1

    # 지렁이 구하기
    cnt = 0
    for x in range(X):
        for y in range(Y):
            if matrix[y][x] == 1:
                dfs(x,y)
                cnt +=1 
    
    # 출력
    print(cnt)