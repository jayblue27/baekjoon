def solution(n):
    answer = []

    n = str(n)
    for i in n:
        answer.append(int(i)) # int형태로 list에 입력       

    # 마지막 원소부터 처음 원소까지 뒤집기 인덱싱
    answer = answer[::-1]

    return answer