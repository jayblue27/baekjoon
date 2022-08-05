def solution(clothes):
    # 옷 타입별 
    hash_map = {}
    for clothe, clothe_type in clothes:
        hash_map[clothe_type] = hash_map.get(clothe_type, 0) + 1 # 디폴트 딕트 쓴거랑 같은 개념?
    
        
    # 입지 않는 경우를 포함 모든 조합 계산
    answer = 1
    for clothe_type in hash_map:   
        answer *= (hash_map[clothe_type] + 1)
    print(answer)
    
    # 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1
