'''
방별로 P의 코드를 추출
'''

from itertools import combinations

def solution(places):
    answer = []
    # 모든 대기실 순환
    for place in places:
        # 각 대기실 순환
        place_list = []
        for line in place:
            # 원소들 list 형태로 변환
            place_list.append(list(line))
        
        # p_code 확보 (P 좌표)
        p_code = []
        for r in range(5):
            for c in range(5):
                if place_list[r][c] == 'P':
                    p_code.append((r,c))
        
        # p_code 순열생성
        p_combi = combinations(p_code, 2)
        
        # 일반처리
        for a,b in p_combi:
            # 맨하탄 거리 계산
            man = abs(a[0]-b[0]) + abs(a[1]-b[1])
            # 맨하탄 2이하인 경우 조건 확인 
            if man <= 1:
                answer.append(0)
                break
            
            if man == 2:
                # print(a,b)
                # r 같은 경우 -> a[1] + 1 == O(빈테이블 이면) 브레이크 append 0
                if a[0] == b[0]:
                    nc = a[1] + 1
                    r = a[0]
                    if nc < 5 and place_list[r][nc] == 'O':
                        answer.append(0)
                        break
                # c 같은 경우
                if a[1] == b[1]:
                    c = a[1]
                    nr = a[0] + 1
                    if nr < 5 and place_list[nr][c] == 'O':
                        answer.append(0)
                        break
                
                
                # r,c 둘다 다른경우
                if a[0] != b[0] and a[1] != b[1]:
                    # 왼쪽하단 -> 오른쪽상단 대각선
                    if a[0] < b[0] and a[1] > b[1]:
                        c, nc = a[1], a[1] - 1
                        r, nr = a[0], a[0] + 1 
                        
                    else:                    
                        c, nc = a[1], a[1] +1
                        r, nr = a[0], a[0] + 1 

                    
                    if (0<= nr < 5 and place_list[nr][c] == 'O') or (0 <= nc < 5 and place_list[r][nc] == 'O'):
                        answer.append(0)
                        break
                
        else: answer.append(1)

    return answer        
