def solution(phone_book):
    '''
    ㅇ 문제이해
    - 한 번호가 다른 번호의 접두어인가?
    - 어떤 번호가 다른 번호의 접두어가 있는 경우 false 아니면 true
    - phone_book의 길이 1~1,000,000 꽤 크다
    - 중복 없음
    
    ㅇ 접근법
    - hash map
    '''
    # hash map 생성
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 1
    # print(hash_map)
    # 접두어 여부 확인
    for phone_num in phone_book:
        # print(phone_num, num)
        prefix = ''
        for num in phone_num:
            prefix += num
            
            if prefix in hash_map and prefix != phone_num:
                return False
    return True

        
        
    
    
    answer = True
    return answer