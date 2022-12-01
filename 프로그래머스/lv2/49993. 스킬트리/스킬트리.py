'''
스킬트리가 없는 경우 순서에 상관없이 배울 수 있다.
스킬트리 있는 경우 선행스킬을 배워야 다음 스킬을 배울 수 있다. 

큐로 풀어야?

1.스킬트리를 큐(리스트)로 만들고 
2.skill을 순회하면서 스킬트리에 없는 경우 그냥 배우고(popleft)
3.배울 순서가 됐는지 배웠으면 popleft
4. 모든 스킬 배우면 cnt+=1


'''

def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for tree in skill_trees:
        tree_lst = list(tree) # 큐 생성
        skill_lst = list(skill)
        # skill 순회
        
        for s in tree_lst:
            if s not in skill_lst:
                continue
            
            elif s == skill_lst[0]:
                skill_lst.pop(0)
            
            else:
                answer -=1
                break
                
        # print(skill_lst)
            
            
        
    return answer