from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    
    # 한글자만 다를때
    while q:
        word, cnt = q.popleft()
        # 타겟 단어이면 answer 갱신 및 종료
        if word == target:
            answer = cnt
            break        
        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
                    
    return answer