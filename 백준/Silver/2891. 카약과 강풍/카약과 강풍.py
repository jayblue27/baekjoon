# 문제이해
# 손상된 카약수
# 여분을 가지고 있는 카약수

# 카약이 손상됐지만,
# 본인이 여분을 가지고 있거나 앞 뒤로 여분이 있는 경우 
# 빌려서 (-1) 게임 진행 가능
# 게임이 불가능한 팀의 수 구하라

def sol(N, d_list, r_list):
    
    # 아래 조건문에서 바로 리스트에 remove하니까 2개이상 겹치는 경우 넘어가버리는 문제 있어서 틀림
    # removes로 지울 목록 따로 받아둔 다음에 한꺼번에 제거
    removes = []
    for r in r_list:
        if r in d_list:
            removes.append(r)

    for r in removes:
        d_list.remove(r)
        r_list.remove(r)

    d_list.sort()
    r_list.sort()

    cnt = len(d_list)

    #여분 리스트 dp처럼 만들고
    dp = [0] * (N+2)
    for r in r_list:
        dp[r] = 1

    # 데미지 리스트 순회하며 여분리스트 조회하고 있으면 cnt-=1
    for d in d_list:
        if dp[d-1] == 1:
            dp[d-1] = 0
            cnt -= 1
        
        elif dp[d+1] == 1:
            dp[d+1] = 0
            cnt -= 1

    return cnt

if __name__ == '__main__':
    N,D,R = map(int, input().split())
    d_list = list(map(int,input().split()))
    r_list = list(map(int,input().split()))
    

    print(sol(N,d_list,r_list))
