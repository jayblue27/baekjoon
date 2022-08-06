from itertools import product

def solution(word):
    words = []
    for i in range(1, 6): # 1이상 5이하
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(list(c)))

    words.sort()  # 오름차순 정렬
    return words.index(word) + 1 # index 찾기 
