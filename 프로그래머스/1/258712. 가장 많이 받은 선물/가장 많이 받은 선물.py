'''
1. 문제이해
- 이번 달 까지 선물을 주고받은 기록을 바탕으로
- 다음 달에 누가 선물을 많이 받을지 예측
    - 선물을 주고 받은 기록을 바탕으로
    - 선물을 많이 준사람이 다음달에 선물 1개 받음
    
    - 두 사람이 선물을 주고받은 기록이 없거나, 주고 받은 개수가 같다면, 선물 지수가 더 큰사람이 받음

- 선물지수 : 이번 달까지의 기록만 가지고 계산
- 선물지수는 A와 B 말고도 A와 C에서도 발생할 수 있다. 


2. 풀이순서 생각
- (선물지수 계산) 사용자들끼리 주고받은 선물의 수 기록하기
- (다음 달 선물 수 계산) 
    - 주고 받은 선물 있는 경우 
        - 서로간의 선물갯수 이용 다음달에 받을 선물의 수 계산
    - 아닌경우
        - 선물지수 이용해서 계산

'''

def solution(friends, gifts):
    answer = 0
    length = len(friends)
    score = [0] * len(friends)
    
    # 0. 선물계수 테이블 생성 (2차원)
    give = [[0] * length for _ in range(length)] 
    
    # 1. 이번 달 기록 기반, 선물지수 계산
    for gift in gifts:
        # 선물을 준사람 받은사람 구분해서 
        gift = gift.split(" ")
        giver = friends.index(gift[0])
        reciever = friends.index(gift[1])
        
        # 선물지수 계산
        give[giver][reciever] += 1

        
    # 2. 다음 달에 받을 선물의 수 에측하기
    for i in range(length):
        for j in range(i + 1, length):
            give_score = give[i][j] # i가 j에게 준 선물의 개수
            recieve_score = give[j][i] # j에게 받은 선물의 개수

            #1-1. 선물을 주고 받은 경우 -> 주고받은 선물의 수 만으로 다음달 선물 개수 계산
            if (give_score != recieve_score) and (give_score > 0 or recieve_score > 0):
                # i가 받은게 더 많으면?
                if give_score > recieve_score:
                    score[i] += 1
                
                # i가 준게 더 많으면?
                else:
                    score[j] += 1

                    
            #1-2. 두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면,
            else:
                # i입장, j입장에서 준 선물의 수 계산
                giver_present_score = sum(give[i])
                reciever_present_score = sum(give[j])
                
                # 위 변수에 받은 선물의 수 빼기
                for k in range(length):
                    giver_present_score -= give[k][i]
                    reciever_present_score -= give[k][j]

                # i와 j간 선물계수 비교해서 한쪽이 더 큰경우에만 선물+1 시킴
                if giver_present_score > reciever_present_score:
                    score[i] += 1

                elif giver_present_score < reciever_present_score:
                    score[j] += 1

    # 누가 다음달에 가장 선물을 많이 받았는가? 계산
    answer = max(score)
    return answer