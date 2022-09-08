import re
def solution(new_id):
    #1단계 소문자로 변환
    ans = new_id.lower()
    #2단계 소문자, 숫자, -, _, .를 제외한 모든 문자가 제거
    ans = re.sub('[^0-9a-z_.\-]+', '', ans) # ^ :not , + :1회이상 반복
    #3단계 .가 2번 이상 있는거를 .로 바꿈
    ans = re.sub('\.\.+', '.', ans)
    #4단계 .가 처음이나 끝에 있을때는 제거 
    ans = ans.strip('.')
    #5단계 빈 문자열 이라면 a로 대입
    if ans == '': ans = 'a'
    #6단계 id의 길이를 15개로 조절하고 만약에 마지막이 . 이면 제거
    ans = ans[:15].rstrip('.')
    #7단계 길이가 3이 될때까지 마지막 문자 추가 (중요)         
    ans+=ans[-1]*(3-len(ans))
    
    return ans