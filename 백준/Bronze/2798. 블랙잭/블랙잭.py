# 백준 - 블랙잭(부르트포스 알고리즘)
# 3중 for문으로 풀라는데? 
# 제한시간 1초

# 부르트포스 -> 전체를 순회 한다. 무식하게 푼다.
# 카드 3개를 선택
# M을 넘지 않거나 M에 가장 가까운 

#입력
N, M = map(int, input().split())
cards = list(map(int, input().split()))

def black(num, target):
    #임시 합계 변수
    tmp_sum = 0
    # 3장의 카드를 뽑아야 하니까 for문 3번 돈다. (중복 없음)
    # 1번카드 순회 n-2까지
    for i in range(0,num-2):
        # 2번카드 i다음 카드 부터 n-1까지
        for j in range(i+1,num-1):
            # 3번카드 j다음카드 부터 n까지
            for k in range(j+1,num):
                # 3카드의 합계 최대치를 구하기 위한 조건문
                if tmp_sum <= sum([cards[i],cards[j],cards[k]]) < target+1 :
                    # 최대 합계값 갱신
                    tmp_sum = sum([cards[i],cards[j],cards[k]])                    
    return tmp_sum

print(black(N,M))