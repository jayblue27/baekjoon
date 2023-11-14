def solution(a, b):
    a = str(a)
    b = str(b)
    ab = int(a+b)
    ba = int(b+a)
    answer = max(ab, ba)
    return answer