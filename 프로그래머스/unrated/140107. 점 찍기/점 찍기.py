

# 실패
# 규칙이 있는 줄 알았으나 n-1 + ((d//k)+1)
# d가 5이상 넘어가면서 내가 생각한 규칙과는 다른 방식으로 값이 나왔다. 
#   0 1 2  3  4 5 
# 0 1 1 1  1  1 1 -> 0,0 단 하나
# 1 1 3 6 10 15
# 2 1 1 3  3  6
# 3 1 1 1  3  3 
# 4 1 1 1 
# 5

#def solution(k, d):
#    answer = 0
#    #dp = [1]*1000001
#    dp = [1]*(d +1)
#    for i in range(1,d+1):
#        if i%k == 0:
#            dp[i] = dp[i-1] + (i//k) + 1
#        else:
#            dp[i] = dp[i-1]        
#    return dp[d]


# 원의 방정식으로 접근
# https://mathbang.net/454#gsc.tab=0 -> 원의 방정식 설명
# 원의 방정식 : 한 점에서 같은 거리에 있는 점들의 집합
# 언의 중심이 (a,b) 이고 반지름의 길이가 r인 원의 방정식


# 풀이 참조
# https://velog.io/@pindum/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A0%90-%EC%B0%8D%EA%B8%B0-Python

def solution(k, d):
    count = 0
    y = d // k * k
    x = 0
    
    # x좌표가 제한거리 미만이라면
    while x <= d:
        # 가장 큰 원의 내부에 있는 경우
        if x**2 + y**2 <= d**2:
            # 
            count += y//k + 1
            x += k # x좌표 갱신 (k씩 증가)
        # 
        else:
            y -= k
    return count

