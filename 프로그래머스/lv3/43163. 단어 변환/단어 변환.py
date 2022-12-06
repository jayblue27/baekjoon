from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append((begin, 0))
    visited = [False] * len(words)
    
    # 예외처리
    # target이 words에 없으면 변환하지 못한다. 
    if target not in words:
        return 0
    
    # word가 현재 단어랑 1글자만 다를 때 방문처리하고, cnt+=1
    while queue:
        word, cnt = queue.popleft()
        
        # 현재 단어가 target과 일치하면 cnt 반환
        if word == target:
            return cnt
        
        # 불일치인 경우 words 순회하면서        
        for i in range(len(words)):
            temp_cnt = 0 # 몇 글자가 다른지 비교하기 위한 임시 count 변수 (2개 혹은 3개가 다 다르면 안된다.)
            
            # i번째 단어가 이미 비교하지 않았던 단어라면(비교했으면 다시 돌아갈 필요 없음)
            if not visited[i]:
                
                # 현재 단어와 i번째 단어간 서로 다른 철자의 개수를 구해서
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                
                # 철자가 하나만 다른경우 (인접노드라고 판단)
                if temp_cnt == 1:
                    # queue에 i번째 단어와, 증가된 cnt를 append하고
                    queue.append((words[i], cnt+1))
                    visited[i] = True # 방문처리
                    
    