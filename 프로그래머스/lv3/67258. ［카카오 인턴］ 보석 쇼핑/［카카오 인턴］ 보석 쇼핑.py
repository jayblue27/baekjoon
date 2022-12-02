'''
어피치 
스트레스 해소 -> 쇼핑 
특정 범위(슬라이싱?) 싹슬이 구매 

진열된 모드느 종류의 보석을 적어도 1개이상 포함
가장 짧은 구간 찾기

시작 진열대 번호, 끝 진열대 번호 배열에 담아 return 
시작 진열대 번호가 가장 작은 구간 return 

전체 보석의 종류 확보 (길이)

for문 2번 돌면 시간 초과 날듯

투포인터? 

참고함
'''
def solution(gems):
    # 보석종류
    gems_nkind = len(set(gems))
    # 예외처리 종류 1개인 경우 무조건 [1,1]
    if gems_nkind == 1:
        return [1, 1]
    
    # 그외 2포인터
    l, r = 0, 0
    answer = [1, len(gems)]
    gems_dict = dict()
    gems_dict[gems[0]] = 1
    while l < len(gems) and r < len(gems):
        # 모든 보석을 포함하고 있는 경우
        if len(gems_dict) == gems_nkind:
            if answer[1] - answer[0] > r - l:
                answer = [l+1, r+1]
            if gems_dict[gems[l]] != 1:
                gems_dict[gems[l]] -= 1
            else:
                del gems_dict[gems[l]]
            l += 1
        else:
            r += 1
            if r >= len(gems):
                break
            if not gems[r] in gems_dict:
                gems_dict[gems[r]] = 1
            else:
                gems_dict[gems[r]] += 1
    return answer
    
    