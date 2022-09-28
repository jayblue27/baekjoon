def solution(s):
    tmp = [*map(int,s.split())]
    return f'{min(tmp)} {max(tmp)}'

