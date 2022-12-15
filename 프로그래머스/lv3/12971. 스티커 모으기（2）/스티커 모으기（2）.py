'''
dp문제? -> 경우의 수를 줄여주는 알고리즘
30분 고민하고 모르겠으면 다양한 풀이들을 보고 배워라

1. 첫번째 수를 사용하는 경우 -> 마지막 수 사용불가
2. 첫번째 수 사용하지 않는경우 -> 마지막 수 사용가능

두가지 경우가 있어서 dp를 2차원으로 설정
'''

def solution(sticker):
    size = len(sticker)
    # 예외처리 
    if size == 1: 
        return sticker[0]
    
    # dp 테이블 초기화
    dp = [[0 for _ in range(size)] for _ in range(2)]
    
    # 첫번째 수 사용하는 경우 
    dp[0][0] = sticker[0] # 첫번째 수 
    dp[0][1] = sticker[0] # 두번째 못쓰니까 첫번째 수랑 같게 설정

    for i in range(2, size-1): # range-1
        dp[0][i] = max(dp[0][i-2]+sticker[i], dp[0][i-1]) # dp[i-1]의 값 vs dp[i-2] + sticker[i]
    
    # 첫번째 수 사용하지 않는 경우
    dp[1][1] = sticker[1] # 두번째 수 부터 진행 
    
    for i in range(2, size): # full range
        dp[1][i] = max(dp[1][i-2]+sticker[i], dp[1][i-1]) # i-1의 값 vs i + i-2
    
    # print(sticker, sticker)
    # print(dp)
    answer = max(dp[0][size-2], dp[1][size-1])
    return answer