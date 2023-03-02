# 공백을 지우는게 아니라 유지했어야 한다는게 함정

def solution(s):
    tmp1 = s.split(" ")
    tmp2 = [x.lower().capitalize() for x in tmp1]
    return ' '.join(tmp2)
    # return tmp1
    