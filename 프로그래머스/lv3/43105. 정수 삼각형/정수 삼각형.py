def solution(triangle):
    # triangle 뒤집기
    triangle.reverse()
    
    # dp 초기화
    dp = triangle[0]
    
    # 뒤집힌 triangle 길이만큼 순환
    for i in range(len(triangle)):
        # i번째 triangle의 길이-1 만큼 순환
        for j in range(len(triangle[i])-1):
            # j번째와 j+1번째 숫자에
            # i+1번째 triangle의 j번째 숫자와 각각 더한 값 중 큰 값을 dp에 갱신한다.
            dp[j] = max(dp[j] + triangle[i+1][j], dp[j+1] + triangle[i+1][j])
    # 모든 계산이 끝난뒤 첫번째 원소가 최대 값
    return dp[0]